import itertools

cards = open("2023/04/scratchcards.txt", "r").readlines()

scores = []

num_cards = [1 for _ in cards]

for j, card in enumerate(cards):
    winners, numbers = card.split(":")[1].split("|")
    winners = winners.strip().split()
    numbers = numbers.strip().split()
    matches = [n for n in numbers if n in winners]
    if len(matches) > 0:
        scores.append(2**(len(matches) - 1))
    for i in range(len(matches)):
        num_cards[j + i + 1] += num_cards[j]



# def process_cards(indices):
#     matched_indices = []
#     for i, card in enumerate([cards[j] for j in indices if j <= len(cards) - 1]):
#         print(i)
#         winners, numbers = card.split(":")[1].split("|")
#         winners = winners.strip().split()
#         numbers = numbers.strip().split()
#         num_matches = len([n for n in numbers if n in winners])
#         if num_matches == 0:
#             continue
#         else:
#             matched_indices += process_cards(list(range(i+1, i+num_matches+1)))
#     return matched_indices

# matches_dict = {}
# non_wins = []

# for i, card in enumerate(cards):
#     if i != len(cards) - 1:
#         winners, numbers = card.split(":")[1].split("|")
#         winners = winners.strip().split()
#         numbers = numbers.strip().split()
#         num_matches = len([n for n in numbers if n in winners])
#         if num_matches > 0 and i + num_matches < len(cards):
#             matches_dict[i] = list(range(i+1, i+num_matches+1))
#         else:
#             non_wins.append(i)

# # new_cards = process_cards(list(range(len(cards))))
# matches_keys = list(matches_dict.keys())
# matches_keys.reverse()

# while len(matches_keys) != 0:
#     for i, match in enumerate(matches_keys):
#         if not all([x in non_wins for x in matches_dict[match]]):
#             matches_dict[match] = list(itertools.chain(*[matches_dict[m] if (m in matches_keys) else [m] for m in matches_dict[match]]))
#         else:
#             matches_keys.pop(i)
#     print(len(matches_keys))
    

print(scores)