from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MemberForm, FirstTimerForm
from .models import Member, FirstTimer

# Homepage View
def homepage(request):
    return render(request, 'homepage.html')

# Admin Dashboard (Now Requires Login)
@login_required
def admin_dashboard(request):
    members = Member.objects.all()
    first_timers = FirstTimer.objects.all()
    return render(request, 'admin_dashboard.html', {'members': members, 'first_timers': first_timers})

# Admin Login View
def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect upon successful login
        else:
            error_message = "Invalid username or password."
            return render(request, "admin_login.html", {"error_message": error_message})

    return render(request, "admin_login.html")

# Admin Logout View
@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# Add Member View
def add_member(request):
    success_message = None
    form = MemberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        success_message = "Member added successfully!"
        form = MemberForm()  # Reset form after success
    return render(request, 'add_member.html', {'form': form, 'success_message': success_message})

# Add First-Time Visitor View
def add_first_timer(request):
    success_message = None
    form = FirstTimerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        success_message = "First-time visitor registered successfully!"
        form = FirstTimerForm()  # Reset form after success
    return render(request, 'add_first_timer.html', {'form': form, 'success_message': success_message})

# Edit Member View
@login_required
def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(request.POST or None, instance=member)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'edit_member.html', {'form': form, 'member': member})

# Delete Member View (Now with CSRF protection)
@login_required
def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_member.html', {'member': member})

# Edit First-Time Visitor View
@login_required
def edit_first_timer(request, pk):
    first_timer = get_object_or_404(FirstTimer, pk=pk)
    if request.method == "POST":
        form = FirstTimerForm(request.POST, instance=first_timer)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FirstTimerForm(instance=first_timer)
    return render(request, 'edit_first_timer.html', {'form': form})

# Delete First-Time Visitor View (With CSRF protection)
@login_required
def delete_first_timer(request, pk):
    first_timer = get_object_or_404(FirstTimer, pk=pk)
    if request.method == "POST":
        first_timer.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_first_timer.html', {'first_timer': first_timer})

# ✅ Print Church Members
def print_members(request):
    members = Member.objects.all()
    return render(request, "print_members.html", {"members": members})

# ✅ Print First-Time Visitors
def print_first_timers(request):
    first_timers = FirstTimer.objects.all()
    return render(request, "print_first_timers.html", {"first_timers": first_timers})