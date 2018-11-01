from django.urls import path

from .views import (
    LeaveListView,
    LeaveUpdateView,
    LeaveDetailView,
    LeaveDeleteView,
    LeaveCreateView,
    RoleListView,
    RoleUpdateView,
    RoleDetailView,
    RoleDeleteView,
    RoleCreateView,
    ShiftListView,
    ShiftUpdateView,
    ShiftDetailView,
    ShiftDeleteView,
    ShiftCreateView,
    ShiftRuleListView,
    ShiftRuleUpdateView,
    ShiftRuleDetailView,
    ShiftRuleDeleteView,
    ShiftRuleCreateView,
    StaffRuleListView,
    StaffRuleUpdateView,
    StaffRuleDetailView,
    StaffRuleDeleteView,
    StaffRuleCreateView,
    TimeslotListView,
    TimeslotUpdateView,
    TimeslotDetailView,
    TimeslotDeleteView,
    TimeslotCreateView,
)

urlpatterns = [
    path('leave/<int:pk>/edit/',
         LeaveUpdateView.as_view(), name='leave_edit'),
    path('leave/<int:pk>/',
         LeaveDetailView.as_view(), name='leave_detail'),
    path('leave/<int:pk>/delete/',
         LeaveDeleteView.as_view(), name='leave_delete'),
    path('leave/new/', LeaveCreateView.as_view(), name='leave_new'),
    path('leave/', LeaveListView.as_view(), name='leave_list'),
    path('role/<int:pk>/edit/',
         RoleUpdateView.as_view(), name='role_edit'),
    path('role/<int:pk>/',
         RoleDetailView.as_view(), name='role_detail'),
    path('role/<int:pk>/delete/',
         RoleDeleteView.as_view(), name='role_delete'),
    path('role/new/', RoleCreateView.as_view(), name='role_new'),
    path('shift/', RoleListView.as_view(), name='shift_list'),
    path('shift/<int:pk>/edit/',
         ShiftUpdateView.as_view(), name='shift_edit'),
    path('shift/<int:pk>/',
         ShiftDetailView.as_view(), name='shift_detail'),
    path('shift/<int:pk>/delete/',
         ShiftDeleteView.as_view(), name='shift_delete'),
    path('shift/new/', ShiftCreateView.as_view(), name='shift_new'),
    path('shift/', ShiftListView.as_view(), name='shift_list'),
    path('shift_rule/<int:pk>/edit/',
         ShiftRuleUpdateView.as_view(), name='shift_rule_edit'),
    path('shift_rule/<int:pk>/',
         ShiftRuleDetailView.as_view(), name='shift_rule_detail'),
    path('shift_rule/<int:pk>/delete/',
         ShiftRuleDeleteView.as_view(), name='shift_rule_delete'),
    path('shift_rule/new/', ShiftRuleCreateView.as_view(), name='shift_rule_new'),
    path('shift_rule/', ShiftRuleListView.as_view(), name='shift_rule_list'),
    path('leave/<int:pk>/edit/',
         StaffRuleUpdateView.as_view(), name='staff_rule_edit'),
    path('staff_rule/<int:pk>/',
         StaffRuleDetailView.as_view(), name='staff_rule_detail'),
    path('staff_rule/<int:pk>/delete/',
         StaffRuleDeleteView.as_view(), name='staff_rule_delete'),
    path('staff_rule/new/', StaffRuleCreateView.as_view(), name='staff_rule_new'),
    path('staff_rule/', StaffRuleListView.as_view(), name='staff_rule_list'),
    path('timeslot/<int:pk>/edit/',
         TimeslotUpdateView.as_view(), name='timeslot_edit'),
    path('timeslot/<int:pk>/',
         TimeslotDetailView.as_view(), name='timeslot_detail'),
    path('timeslot/<int:pk>/delete/',
         TimeslotDeleteView.as_view(), name='timeslot_delete'),
    path('timeslot/new/', TimeslotCreateView.as_view(), name='timeslot_new'),
    path('timeslot/', TimeslotListView.as_view(), name='timeslot_list'),
]
