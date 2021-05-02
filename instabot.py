

from instapy import InstaPy
from instapy.util import smart_run

insta_username='Naveli_tara'
insta_password='Krishna7'

session=InstaPy(username=insta_username,
                password=insta_password,
                headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    min_followers=150,
                                    min_following=100)

    session.set_do_comment(enabled=True,percentage=100)
    session.set_comments(['WoW!! Wir sind ein Indisch-Deutsches Startup,das wunderschönen Schmuck nach Deutschland bringt!! Schau doch mal bei uns vorbei:)','Hey!! we are a Indian-German Startup, that brings beautiful handmade Indian jewellery to Germany!! Check out our Collection :)'])
    session.like_by_tags(["ohrringe","schmuck","halskette","leipzig","follow","followback"], amount=9)

    session.set_user_interact(amount=10,randomize=True,percentage=100)
    # session.set_do_follow(enabled=True,percentage=25)
    session.set_do_like(enabled=True,percentage=100)
    # session.set_comments(['Really interesting stuff','Nice Work','Appreciate your work'])
    # session.set_do_comment(enabled=True,percentage=100)
    session.interact_user_followers(['marienasemann','fairfashionbag'],amount=100,randomize=True)

session.end()













