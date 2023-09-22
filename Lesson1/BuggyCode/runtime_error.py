def make_quote(sentence,cited):
    return '"'+sentence+'" - '+cited

sentence="There are only two hard things in Computer Science: cache invalidation and naming things."
name="Phil Karlton"

quotes=[("There are only two hard things in Computer Science: cache invalidation and naming things.","Phil Karlton"),("Something anonymous",None)]

for sentence,name in quotes:
    quote=make_quote(sentence,name)
    print(quote)
