from django.urls import path
from .views import (
    VendorListCreateView, VendorRetrieveUpdateDestroyView,
    PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDestroyView,
    vendor_detail, update_vendor
)

urlpatterns = [
    # API endpoints
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-retrieve-update-destroy'),

    # Custom views
    path('vendors/<int:vendor_id>/', vendor_detail, name='vendor-detail'),
    path('vendors/<int:vendor_id>/update/', update_vendor, name='update-vendor'),
]
