from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, login_view, register_view, logout_view, create_recipe, view_recipe, edit_recipe, \
    delete_recipe, view_all_recipes

urlpatterns = [
                  path('', index, name='index'),
                  path('accounts/login/', login_view, name='login_view'),
                  path('register/', register_view, name='register_view'),
                  path('logout/', logout_view, name='logout_view'),
                  path('recipes/create/', create_recipe, name='create_recipe'),
                  path('recipes/<int:recipe_id>/', view_recipe, name='view_recipe'),
                  path('recipes/edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
                  path('recipes/delete/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
                  path('recipes/all/', view_all_recipes, name='view_all_recipes'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
