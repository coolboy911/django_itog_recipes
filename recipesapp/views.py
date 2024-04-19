from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, CreateRecipe
from .models import Recipe


# Create your views here.


def index(request, warning_message=None):
    recipes = Recipe.objects.order_by('?')[:5]
    context = {'recipes': recipes, 'warning_message': warning_message}
    return render(request, 'recipesapp/show_recipes_short.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                message = 'Неправильный логин или пароль, попробуйте ещё раз'
    else:
        message = 'Введите данные'
        form = LoginForm()
    return render(request, 'recipesapp/login_form.html', context={'form': form, 'message': message})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'recipesapp/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def view_recipe(request, recipe_id):
    # recipe = Recipe.objects.filter(pk=recipe_id).first()
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not recipe:
        return redirect('index')
    context = {'recipe': recipe}
    return render(request, 'recipesapp/view_recipe_full.html', context)


def view_all_recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipesapp/view_all_recipes.html', context)


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']
            author = request.user
            recipe = Recipe(name=name, description=description, cooking_steps=cooking_steps,
                            cooking_time=cooking_time, image=image, author=author)
            recipe.save()
            return redirect('index')
    else:
        form = CreateRecipe()
    return render(request, 'recipesapp/create_edit_recipe.html', context={'form': form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author != request.user:  # checking ownership
        return redirect('index')
    if request.method == 'POST':
        form = CreateRecipe(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']

            # rewriting existing recipe
            recipe.name = name
            recipe.description = description
            recipe.cooking_steps = cooking_steps
            recipe.cooking_time = cooking_time
            recipe.image = image
            recipe.save()
            return redirect('index')
    else:
        form = CreateRecipe()
    return render(request, 'recipesapp/create_edit_recipe.html', context={'form': form})


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author != request.user:  # checking ownership
        return redirect('index')
    if recipe is not None:
        recipe.delete()
        return redirect('index')

