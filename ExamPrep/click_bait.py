from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_articles = [int(x) for x in input().split()]
target = int(input())
final_feed = []
while suggested_links and featured_articles:
    current_suggested = suggested_links.popleft()
    current_featured = featured_articles.pop()
    remainder = max(current_suggested, current_featured) % min(current_suggested, current_featured)
    if current_featured == current_suggested:
        final_feed.append(0)
    elif current_featured > current_suggested:
        final_feed.append(abs(remainder))
        if remainder != 0:
            featured_articles.append(remainder * 2)
    else:
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)

print(f'Final Feed: {", ".join(map(str, final_feed))}')
if sum(final_feed) >= target:
    print(f'Goal achieved! Engagement Value: {sum(final_feed)}')
else:
    print(f'Goal not achieved! Short by: {target - sum(final_feed)}')
