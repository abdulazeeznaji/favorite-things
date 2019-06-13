How long did you spend on the coding test below? What would you add to your solution if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.

I did't use Alembic or any other migration framework. In that case  db.create_all(), which looks at models and creates the corresponding tables in our database
Using Alembic, we have a little bit of extra work when we start, but it pays off because it simplifies our workflow for our upgrades.



