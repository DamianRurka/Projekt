from kivy_garden.mapview import MapView


class MyMapView(MapView):
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print("DOWN")

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        print("UP")

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
