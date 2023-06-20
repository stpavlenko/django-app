from django.contrib import admin


from .models import Restaurant, Table, Reservation, Review, MenuItem, Staff


class ReservationInline(admin.TabularInline):
    model = Reservation


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name')
    list_filter = ('address',)
    fields = ['name', 'address', 'description']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'date', 'start_time',
                    'end_time', 'get_restaurant_name')
    list_filter = ('user', 'table__restaurant', 'date')
    list_display_links = ('id', 'table')
    search_fields = ('user', 'date')
    date_hierarchy = 'date'

    @admin.display(description='Ресторан')
    def get_restaurant_name(self, obj):
        return obj.table.restaurant.name


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'number', 'capacity')
    list_filter = ('restaurant', 'capacity')
    inlines = (ReservationInline, )
    # filter_horizontal = ('reservations', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'rating', 'comment', 'date')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name', 'price')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'first_name', 'last_name', 'position',
                    'contact_number')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'contact_number')
    ordering = ('last_name',)
