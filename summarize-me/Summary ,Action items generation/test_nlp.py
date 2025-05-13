from nlp_processing import generate_summary, extract_action_items

# Test transcript
transcript_text = """
I'll start again. Uh, thank you very much. Uh, this is the RM of Springfield meeting agenda uh for April 8th of 2025,
a committee of the whole, uh, starting at exactly 1 p.m. Um, I'd like to do the introductions and myself, I'm Mayor Patrick Terian,
and to my right in descending order is Deputy Mayor Glenn Feu, Ward one. Ward two is Andy Kaczynski. The next will be Ward 3, Mark Miller,
next will be Ward 4. Excuse me, Melinda Warren. And uh I wonder if uh we'll go to the proof of the gender.
Is there any amendments or deletions uh to that from the council? And I see none, and then I get a show of hands and also support.
Unanimous, it's carried, and we'll go to approval of the minutes. Um, that's a committee of the whole minutes, uh, from the last time
that'll be on March 11th. Uh, any additions, deletions uh to the minutes at all? And I see none. I'm just going to show of hands,
those in support. Yeah I know it sounds good. Uh, then we'll go to and finish a business. Uh, first one will be a 6.1,
that's the use of firearms uh bylaw, the draft use. Any discussions on that at all? Yeah, so this came to counsel at a previous
committee of the whole. Um, there was just a few suggestions on this, so we've brought back some changes. They've been tracked
in the bylaws, so council can see what's changed. Uh, there was a request to define um center of fire rifle ammo, so that has
been included there. Um, other changes, um, we talked about the shooting range and shooting gallery, so there's a slight change
that says, does not include shooting gallery was removed, uh, because that is proposed within the new, uh, zoning bylaw,
so we've removed that. Uh, we've just removed high-powered, um, because now we're just talking about center fire rifle.
So there's a few places where higher powered rifle is removed. And then just some um sections of the numbering had to be updated,
so you'll see some numbering change, and then a slight change to add and the discharge of a firearm is not occurring in game areas 34A or 38,
so that was added in. Uh, there was also discussion on the very last page about uh fine amounts that they may be were too low,
so we did look at comparables, uh, and have uh suggested some increases to those fine amounts. So that's the bulk of the,
the changes that um we went with after initial discussions with council.
"""

# Run Summary
summary = generate_summary(transcript_text)
print("\n📄 Summary:\n", summary)

# Run Action Item Extraction
action_items = extract_action_items(summary)
print("\n✅ Action Items:\n", action_items)
