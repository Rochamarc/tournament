from db.base_controller import BaseController


class MainController(BaseController):
    @classmethod
    def select_competitions(cls) -> list[set]:
        """Select all att form competitions table

        Returns
        -------
            A list of sets with competitions info
        """

        return cls.select_register(cls.get_query('select', 'select_competitions'))

    @classmethod
    def select_clubs(cls) -> list[set]:
        """Select all att form clubs table

        Returns
        -------
            A list of sets with clubs info
        """

        return cls.select_register(cls.get_query('select', 'select_clubs'))