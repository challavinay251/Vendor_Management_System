from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return JsonResponse({
        'name': vendor.name,
        'contact_details': vendor.contact_details,
        'address': vendor.address,
        'vendor_code': vendor.vendor_code,
        'on_time_delivery_rate': vendor.on_time_delivery_rate,
        'quality_rating_avg': vendor.quality_rating_avg,
        'average_response_time': vendor.average_response_time,
        'fulfillment_rate': vendor.fulfillment_rate,
    })

def update_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    # Assuming data is sent via POST request
    if request.method == 'POST':
        vendor.name = request.POST.get('name')
        vendor.contact_details = request.POST.get('contact_details')
        vendor.address = request.POST.get('address')
        vendor.save()
        return JsonResponse({'message': 'Vendor updated successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for updating vendor'})

def purchase_order_detail(request, purchase_order_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=purchase_order_id)
    return JsonResponse({
        'po_number': purchase_order.po_number,
        'vendor': purchase_order.vendor.name,
        'order_date': purchase_order.order_date,
        'delivery_date': purchase_order.delivery_date,
        'items': purchase_order.items,
        'quantity': purchase_order.quantity,
        'status': purchase_order.status,
        'quality_rating': purchase_order.quality_rating,
        'issue_date': purchase_order.issue_date,
        'acknowledgment_date': purchase_order.acknowledgment_date,
    })

def update_purchase_order(request, purchase_order_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=purchase_order_id)
    # Assuming data is sent via POST request
    if request.method == 'POST':
        purchase_order.po_number = request.POST.get('po_number')
        purchase_order.order_date = request.POST.get('order_date')
        purchase_order.delivery_date = request.POST.get('delivery_date')
        purchase_order.items = request.POST.get('items')
        purchase_order.quantity = request.POST.get('quantity')
        purchase_order.status = request.POST.get('status')
        purchase_order.quality_rating = request.POST.get('quality_rating')
        purchase_order.save()
        return JsonResponse({'message': 'Purchase order updated successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for updating purchase order'})
