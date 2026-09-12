from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer

from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Product

def home_view(request):
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({"message": "Use /api/v1/ for JSON API access"})
        
    products = Product.objects.filter(is_active=True)[:12]
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'home.html', {'products': products, 'categories': categories})

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['parent']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params.get('parent__isnull') == 'true':
            queryset = queryset.filter(parent__isnull=True)
        return queryset

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related('category').prefetch_related('variants', 'images')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'category__slug']
    search_fields = ['name', 'description']
    ordering_fields = ['base_price', 'created_at']

    @action(detail=True, methods=['get'])
    def variants(self, request, pk=None):
        product = self.get_object()
        variants = product.variants.filter(stock__gt=0)
        serializer = ProductVariantSerializer(variants, many=True)
        return Response(serializer.data)
