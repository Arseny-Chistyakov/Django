from django.urls import path

from admins.views import index, UserAdminListView, UserAdminCreateView, admin_users_update, admin_users_delete, \
    ProductAdminListView, ProductAdminCreateView, admin_products_update, admin_products_delete

app_name = "admins"

urlpatterns = [
    path("", index, name="index"),
    path("users/", UserAdminListView.as_view(), name="admin_users"),
    path("users-create/", UserAdminCreateView.as_view(), name="admin_users_create"),
    path("users-update/<int:pk>/", admin_users_update, name="admin_users_update"),
    path("users-delete/<int:pk>/", admin_users_delete, name="admin_users_delete"),

    path("products/", ProductAdminListView.as_view(), name="admin_products"),
    path("products-create/", ProductAdminCreateView.as_view(), name="admin_products_create"),
    path("products-update/<int:pk>/", admin_products_update, name="admin_products_update"),
    path("products-delete/<int:pk>/", admin_products_delete, name="admin_products_delete"),
]
