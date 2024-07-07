from django.contrib.auth.decorators import user_passes_test


def group_required(group_name):
    def in_group(user):
        """
            Create a custom decorator to check group membership
            allows you to check if a user belongs to a specific group or is a superuser (admin)
        """
        if user.is_authenticated:
            return user.groups.filter(name=group_name).exists() or user.is_superuser
        return False
    return user_passes_test(in_group)




