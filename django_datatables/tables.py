from .models import Table as TableModel
import random
import string

class Table:
    # SLOTS
    __slots__ = [
        '__is_ajax',
        '__style',
        '__queryset',
        '__rows',
        '__load_jquery',
        '__id'
    ]

    # STYLES DEFS
    STYLE_BS3 = 'bootstrap'
    STYLE_BS4 = 'bootstrap4'
    STYLE_JQUERY = 'jqueryui'
    STYLE_FOUNDATION = 'foundation'
    STYLE_SEMANTIC = 'semanticui'
    STYLE_BASE = 'jquery'

    # PROPERTIES
    @property
    def pk(self):
        return self.__id

    @property
    def load_jquery(self):
        return self.__load_jquery

    @property
    def object_list(self):
        return self.__queryset

    @property
    def is_ajax(self):
        return self.__is_ajax

    @property
    def header(self):
        """

        :return:
        """
        header = self.__rows
        return header

    @property
    def html_header(self):
        return self.__get_header_tags()

    @property
    def html_body(self):
        tr = "<tr>{}</tr>"
        td = "<td>{}</td>"

        tds = []
        response = ""
        for item in self.__queryset:
            print(item.__dict__)
            filled_td = (td * len(self.header)) \
                            .format(*[f"%({r})s" for r in self.header]) % \
                        {a: getattr(item, a) for a in dir(item) if not callable(a) and a in self.header}
            response += tr.format(filled_td)

        return response

    # CONSTRUCTOR------------------------------------------------------------------------------------------------
    def __init__(self, queryset, rows: list = [], is_ajax: bool = False, style: str = STYLE_BASE, load_jquery = False):
        self.__queryset = queryset
        self.__is_ajax = is_ajax
        self.__style = style
        self.__load_jquery = load_jquery

        # GENERATE ID
        self.__id = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

        if not rows:
            self.__rows = self.__get_default_rows()
        else:
            self.__rows = rows

        print(self.__rows)

    # OTHER METHODS
    def __get_header_tags(self):
        """
        RETURN HTML OF TABLE HEADER
        :return:
        """
        tag = "<th>{}</th>"

        return (tag * len(self.__rows)).format(*self.__rows)

    def __get_default_rows(self):
        """
        IF NO ROWS PASSED, GET ALL FIELDS FROM MODEL
        :return:
        """

        return [f.name for f in self.__queryset.model._meta.get_fields()]

    def get_style(self):
        return self.__style

    def get_fw_src_css(self):
        """
        RETURN FILENAME OF THE FRAMEWORK CSS FILE (ex: semantic.css)
        :return:
        """
        return f"dtables/css/{self.get_style()}.css"

    def get_dt_src_css(self):
        """
        RETURN FILENAME OF DATATABLE FILE WITH CSS (ex: dataTables.semantic.css)
        :return:
        """
        if self.get_style() != self.STYLE_BASE:
            return f"dtables/css/dataTables.{self.get_style()}.css"
        else:
            return f"dtables/css/{self.get_style()}.dataTables.css"

    def get_src_js(self):
        """
        RETURN THE FILENAME WITH JS
        :return:
        """
        if self.get_style() != self.STYLE_BASE:
            return f"dtables/js/dataTables.{self.get_style()}.js"
        else:
            return f"dtables/js/{self.get_style()}.dataTables.js"
