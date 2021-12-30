from kivy_garden.mapview import MapView, MarkerMapLayer


class MyMapView(MapView):
    def on_touch_down(self, touch):
        for child in self.children[:]:
            if isinstance(child, MarkerMapLayer):
                if child.dispatch('on_touch_down', touch):
                    return True

    def on_touch_up(self, touch):
        for child in self.children[:]:
            if isinstance(child, MarkerMapLayer):
                if child.dispatch('on_touch_up', touch):
                    return True

    def on_touch_move(self, touch):
        pass
