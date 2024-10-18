import viktor as vkt


class Parametrization(vkt.Parametrization):
    welcome = vkt.Text("# 👋 Welcome to your first VIKTOR app! 👋\n## Let's start with the basics")
    length = vkt.NumberField("Length", default=1)
    width = vkt.NumberField("Width", default=1)
    height = vkt.NumberField("Height", default=1)


class Controller(vkt.Controller):
    parametrization = Parametrization

    @vkt.TableView("Results")
    def results(self, params, **kwargs):
        data = [
            [1, 2],
            [3, 4],
        ]
        row_headers = ["Row 1", "Row 2"]
        column_headers = ["Col 1", "Col 2"]
        return vkt.TableResult(data, row_headers=row_headers, column_headers=column_headers)