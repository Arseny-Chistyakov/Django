from django.urls import path

from admins.views import index, UserAdminListView, UserAdminCreateView, UserAdminUpdateView, UserAdminDeleteView, \
    ProductAdminListView, ProductAdminCreateView, ProductAdminUpdateView, ProductAdminDeleteView

app_name = "admins"

urlpatterns = [
    path("", index, name="index"),
    path("users/", UserAdminListView.as_view(), name="admin_users"),
    path("users-create/", UserAdminCreateView.as_view(), name="admin_users_create"),
    path("users-update/<int:pk>/", UserAdminUpdateView.as_view(), name="admin_users_update"),
    path("users-delete/<int:pk>/", UserAdminDeleteView.as_view(), name="admin_users_delete"),

    path("products/", ProductAdminListView.as_view(), name="admin_products"),
    path("products-create/", ProductAdminCreateView.as_view(), name="admin_products_create"),
    path("products-update/<int:pk>/", ProductAdminUpdateView.as_view(), name="admin_products_update"),
    path("products-delete/<int:pk>/", ProductAdminDeleteView.as_view(), name="admin_products_delete"),
]
