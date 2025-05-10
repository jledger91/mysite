class DynamicFieldsSerializerMixin:
    """
    A Mixin that allows dynamic modification of serializer fields
    based on the request user, instance, or view context.
    """

    dynamic_field_rules = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get("request")
        view = self.context.get("view")
        user = getattr(request, "user", None)
        instance = self.instance

        if not instance and view and hasattr(view, "get_object"):
            try:
                instance = view.get_object()
            except Exception:
                instance = None

        self.apply_dynamic_field_rules(user, instance)

    def apply_dynamic_field_rules(self, user, instance):
        """
        Applies the dynamic_field_rules defined in the serializer.
        Should pop fields based on user/instance conditions.
        """

        for field_name, rule_func in self.dynamic_field_rules.items():
            if not rule_func(user, instance):
                self.fields.pop(field_name, None)
