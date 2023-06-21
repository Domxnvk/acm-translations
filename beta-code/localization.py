
    @commands.slash_command(guild_ids=[1117516168132050974])
    async def numslash(
    inter: disnake.ApplicationCommandInteraction,
        num: int = commands.Param(
            name=Localized(key="add_num.cool_number_name"),
            description=Localized(key="add_num.cool_number_description"),
            default="add_num.cool_number_name"  # Replace with your default value
        )
    ):
        """
        Adds 5 to a number.

        Parameters
        ----------
        num: Some number
        """
        print(Localized(key="add_num.name"))
        print(Localized(key="add_num.description"))
        print(Localized(key="add_num.cool_number_name"))
        print(Localized(key="add_num.cool_number_description"))
        await inter.response.send_message(f"{num} + 5 = {num + 5}")
