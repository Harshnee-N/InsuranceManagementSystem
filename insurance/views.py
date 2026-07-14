from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Customer, Policy, CustomerPolicy, Claim
from .forms import UserRegisterForm, CustomerForm, ClaimForm, PolicyForm


def home(request):
    policies = Policy.objects.all()
    return render(request, 'insurance/home.html', {'policies': policies})


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserRegisterForm()
        customer_form = CustomerForm()

    return render(request, 'insurance/register.html', {
        'user_form': user_form,
        'customer_form': customer_form,
    })


@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')

    customer = Customer.objects.filter(user=request.user).first()

    if customer is None:
        return redirect('home')

    policies = CustomerPolicy.objects.filter(customer=customer)
    claims = Claim.objects.filter(customer_policy__customer=customer)

    return render(request, 'insurance/dashboard.html', {
        'policies': policies,
        'claims': claims,
    })


@login_required
def buy_policy(request, policy_id):
    customer = Customer.objects.filter(user=request.user).first()

    if customer is None:
        return redirect('register')

    policy = get_object_or_404(Policy, id=policy_id)

    already_bought = CustomerPolicy.objects.filter(
        customer=customer,
        policy=policy,
        is_active=True
    ).exists()

    if not already_bought:
        CustomerPolicy.objects.create(customer=customer, policy=policy)

    return redirect('dashboard')


@login_required
def make_claim(request, customer_policy_id):
    customer = Customer.objects.filter(user=request.user).first()

    if customer is None:
        return redirect('register')

    customer_policy = get_object_or_404(
        CustomerPolicy,
        id=customer_policy_id,
        customer=customer
    )

    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.customer_policy = customer_policy
            claim.save()
            return redirect('dashboard')
    else:
        form = ClaimForm()

    return render(request, 'insurance/make_claim.html', {'form': form})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')

    total_policies = Policy.objects.count()
    total_customers = Customer.objects.count()
    total_claims = Claim.objects.count()
    pending_claims = Claim.objects.filter(status='Pending').count()
    active_customer_policies = CustomerPolicy.objects.filter(is_active=True).count()
    recent_claims = Claim.objects.select_related(
        'customer_policy__customer__user',
        'customer_policy__policy'
    ).order_by('-claim_date', '-id')[:5]

    return render(request, 'insurance/admin_dashboard.html', {
        'total_policies': total_policies,
        'total_customers': total_customers,
        'total_claims': total_claims,
        'pending_claims': pending_claims,
        'active_customer_policies': active_customer_policies,
        'recent_claims': recent_claims,
    })


@login_required
def add_policy(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PolicyForm()

    return render(request, 'insurance/add_policy.html', {'form': form})


@login_required
def manage_policies(request):
    if not request.user.is_staff:
        return redirect('home')

    policies = Policy.objects.order_by('policy_type', 'name')
    return render(request, 'insurance/manage_policies.html', {'policies': policies})


@login_required
def edit_policy(request, policy_id):
    if not request.user.is_staff:
        return redirect('home')

    policy = get_object_or_404(Policy, id=policy_id)

    if request.method == 'POST':
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            return redirect('manage_policies')
    else:
        form = PolicyForm(instance=policy)

    return render(request, 'insurance/add_policy.html', {
        'form': form,
        'policy': policy,
        'form_title': 'Edit Insurance Policy',
        'button_label': 'Update Policy',
    })


@login_required
def delete_policy(request, policy_id):
    if not request.user.is_staff:
        return redirect('home')

    policy = get_object_or_404(Policy, id=policy_id)

    if request.method == 'POST':
        policy.delete()
        return redirect('manage_policies')

    return render(request, 'insurance/delete_policy.html', {'policy': policy})


@login_required
def manage_claims(request):
    if not request.user.is_staff:
        return redirect('home')

    claims = Claim.objects.select_related(
        'customer_policy__customer__user',
        'customer_policy__policy'
    ).order_by('-claim_date', '-id')
    return render(request, 'insurance/manage_claims.html', {'claims': claims})


@login_required
def update_claim_status(request, claim_id, status):
    if not request.user.is_staff:
        return redirect('home')

    claim = get_object_or_404(Claim, id=claim_id)
    valid_statuses = {choice[0] for choice in Claim.STATUS_CHOICES}

    if request.method == 'POST' and status in valid_statuses:
        claim.status = status
        claim.save(update_fields=['status'])

    return redirect('manage_claims')


def logout_user(request):
    logout(request)
    return redirect('home')
