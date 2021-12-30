from kivy_garden.mapview import MapLayer
from kivymd.app import MDApp


class LineMapLayer(MapLayer):
    def __init__(self, **kwargs):
        super(LineMapLayer, self).__init__(**kwargs)
        self.zoom = 15

        geo_dover   = [18.455750,-69.970347]
        geo_calais  = [18.456259,-69.966334]

        # NOTE: Points must be valid as they're no longer clamped
        self.coordinates = []


    def newpointgeo(self,longlat):
        longlatx = (longlat[1],longlat[0])
        self.coordinates.append(longlatx)

    def reposition(self):
        mapview = self.parent

        #: Must redraw when the zoom changes
        #: as the scatter transform resets for the new tiles
        if (self.zoom != mapview.zoom):
            self.draw_line()

    def gen_point(self):
        n = len(self.coordinates)
        dx,dy = random.randint(-100,100)/10000.0,random.randint(0,100)/10000.0
        c = (self.coordinates[-1][0]+dx,
             self.coordinates[-1][1]+dy)

        return c

    def add_point(self):
        #: Add a random point close to the previous one
        for i in range(len(self.coordinates)):
            self.coordinates.append(self.gen_point())
        self.draw_line()

    def get_x(self, lon):
        """Get the x position on the map using this map source's projection
        (0, 0) is located at the top left.
        """
        return clamp(lon, MIN_LONGITUDE, MAX_LONGITUDE)

    def get_y(self, lat):
        """Get the y position on the map using this map source's projection
        (0, 0) is located at the top left.
        """
        lat = clamp(-lat, MIN_LATITUDE, MAX_LATITUDE)
        lat = lat * pi / 180.
        return ((1.0 - log(tan(lat) + 1.0 / cos(lat)) / pi))

    def draw_line(self, *args):
        mapview = self.parent
        self.zoom = mapview.zoom

        # When zooming we must undo the current scatter transform
        # or the animation distorts it
        scatter = mapview._scatter
        map_source = mapview.map_source
        sx,sy,ss = scatter.x, scatter.y, scatter.scale
        vx,vy,vs = mapview.viewport_pos[0], mapview.viewport_pos[1], mapview.scale

        # Account for map source tile size and mapview zoom
        ms = pow(2.0,mapview.zoom) * map_source.dp_tile_size

        #: Since lat is not a linear transform we must compute manually
        line_points = []
        for lat,lon in self.coordinates:
            line_points.extend((self.get_x(lon),self.get_y(lat)))
            #line_points.extend(mapview.get_window_xy_from(lat,lon,mapview.zoom))


        with self.canvas:
            # Clear old line
            self.canvas.clear()

            # Undo the scatter animation transform
            Scale(1/ss,1/ss,1)
            Translate(-sx,-sy)

            # Apply the get window xy from transforms
            Scale(vs,vs,1)
            Translate(-vx,-vy)

            # Apply the what we can factor out
            # of the mapsource long,lat to x,y conversion
            Scale(ms/360.0,ms/2.0,1)
            Translate(180,0)

            # Draw new
            Color( 0, 0 , 0 , .8)
            Line(points=line_points , width=4/ms , joint_presicion = 100)#4/ms)#,joint_precision=100)

class YourWorldOnline(MapLayer):

    def build(self):
        self.screen = LineMapLayer()
        return self.screen
