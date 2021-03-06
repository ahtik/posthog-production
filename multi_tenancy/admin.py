from django.contrib import admin

from .models import Plan, OrganizationBilling



@admin.register(OrganizationBilling)
class OrganizationBillingAdmin(admin.ModelAdmin):
    readonly_fields = ("stripe_checkout_session",)
    list_display = (
        "get_organization_name",
        "stripe_customer_id",
        "should_setup_billing",
        "billing_period_ends",
        "plan",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by("should_setup_billing")

    def get_organization_name(self, obj):
        return obj.organization.name


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "name",
        "price_id",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by("key")
