from .imports import *



class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class SignUpView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, "staff_sign_up.html", {"form": UserCreationForm})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("customer_list")

            except IntegrityError:
                return render(
                    request,
                    "staff_sign_up.html",
                    {"form": UserCreationForm, "error": "Usuario ya existe"},
                )

        return render(
            request,
            "staff_sign_up.html",
            {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
        )


class SignOutView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("index")
               
class SignInView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "staff_sign_in.html", {"form": AuthenticationForm})

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "staff_sign_in.html",
                {
                    "form": AuthenticationForm,
                    "error": "Usuario o Contraseña incorrecto",
                },
            )
        else:
            login(request, user)
            return redirect("customer_list")       




class CustomerList(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            users_all = CustomerModel.objects.filter(
                Q(name__icontains=query)
            )
        else:
            users_all = CustomerModel.objects.all()

        return render(request, "customer_list.html", {"users": users_all})


class CustomerCreateView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, "customer_create_view.html", {"form": CustomerForm})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            form = CustomerForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                return redirect("customer_list")
            else:
                return render(
                    request,
                    "customer_create_view.html",
                    {"form": form, "error": "Proporciona datos válidos"},
                )
        except ValueError:
            return render(
                request,
                "customer_create_view.html",
                {"form": CustomerForm, "error": "Proporciona datos válidos"},
            )
            
class CustomerUpdateView(UpdateView):
    model = CustomerModel
    form_class = CustomerForm
    template_name = 'customer_update_view.html'
    success_url = reverse_lazy('customer_list') 
    

class CustomerDeleteView(DeleteView):
    model = CustomerModel
    success_url = reverse_lazy('customer_list')  
    template_name = 'customer_delete_view.html' 