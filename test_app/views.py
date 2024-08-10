from django.shortcuts import render,redirect
from .models import Parent, Child
from .form import ParentForm, ChildForm

# Create your views here.
def create_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("parent_child_manager")
    return render(request, 'create_parent.html', {'form': ParentForm()})

def create_child(request, parent_id):
    if request.method == 'POST':
        form = ChildForm(request.POST, initial={'parent_id': parent_id})
        form.save()
        return redirect("parent_child_manager")
    form = ChildForm(initial={'parent_id': parent_id})
    return render(request, 'create_child.html', {'form': form, 'parent_id': parent_id})

def edit_child(request, child_id):
    child = Child.objects.get(id=child_id)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        form.save()
        return redirect('parent_child_manager')
    form = ChildForm(instance=child)
    return render(request, 'edit_child.html', {'form': form, 'child_id': child.id})

def parent_child_manager(request):
    parents = Parent.objects.all()
    parent_form = ParentForm()

    # Create a list of tuples (parent, children)
    parents_with_children = []

    for parent in parents:
        children = Child.objects.filter(parent=parent)
        parents_with_children.append((parent, children))

    return render(
        request,
        "parent_child_manager.html",
        {
            "parents_with_children": parents_with_children,
            "parent_form": parent_form,
        },
    )