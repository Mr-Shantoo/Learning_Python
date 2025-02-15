browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
# if we want to check Top.
print(browsing_session[-1])

# for checking if empty or not....
if not browsing_session:
    print("disable")
