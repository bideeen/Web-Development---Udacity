import media
import fresh_tomatoes

toy_story = media.Movie("Toy Stroy",
                        "A story of a boy",
                        "https://www.google.com/search?q=toy+story+4+full+movie&safe=active&biw=656&bih=624&tbm=isch&sxsrf=ACYBGNQG2B0o_c3Lu_ARZwcZKrSqHy59fg:1577699542484&source=lnms&sa=X&ved=0ahUKEwjf2armjN3mAhUPEcAKHccvCvQQ_AUICygC#",
                        "https://www.youtube.com/watch?v=wmiIUN-7qhE"
)
# toy_story.show_trailer()
avatar = media.Movie('Avatar',
                    'A marine on aa alien planet',
                    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.cinemablend.com%2Ffilter%3Ascale%2Fcb%2Fe%2F0%2F3%2F1%2F5%2F7%2Fe03157606201093ca19d72ba68f69a4a4e5c6a04b0810368690c21b0b86019e2.jpg%3Fmw%3D600&imgrefurl=https%3A%2F%2Fwww.cinemablend.com%2Fnew%2FAvatar-Trailer-Shatters-Apple-Download-Records-14481.html&docid=K_bLPP8rEp4MfM&tbnid=p0kKsmpp064VPM%3A&vet=10ahUKEwjh5peHl93mAhUL_RQKHSbTB_oQMwhUKAgwCA..i&w=250&h=293&safe=active&bih=624&biw=656&q=avatar%20movie%20trailer&ved=0ahUKEwjh5peHl93mAhUL_RQKHSbTB_oQMwhUKAgwCA&iact=mrc&uact=8',
                    'https://www.youtube.com/watch?v=5PSNL1qE6VY'
)
# print(avatar.storyline)
mip = media.Movie('Midnight In Paris',
                    'A marine on aa alien planet',
                    'https://www.google.com/imgres?imgurl=https%3A%2F%2Flandofblogging.files.wordpress.com%2F2013%2F06%2Fmidnight-in-paris-locandina-trailer.jpg&imgrefurl=https%3A%2F%2Flandofblogging.wordpress.com%2F2013%2F06%2F11%2Fmidnight-in-paris-2011-movie-review%2F&docid=H0z6MmhjgzwPIM&tbnid=-yvQgF-sqFHdVM%3A&vet=10ahUKEwiD2Y_2lt3mAhVWBGMBHat6BMAQMwhQKAMwAw..i&w=1050&h=1500&safe=active&bih=624&biw=656&q=midnight%20in%20paris%20movie%20trailer&ved=0ahUKEwiD2Y_2lt3mAhVWBGMBHat6BMAQMwhQKAMwAw&iact=mrc&uact=8',
                    'https://www.youtube.com/watch?v=irLRpuUx3jk'
)
ratatouille = media.Movie('Ratatouille',
                    'A marine on aa alien planet',
                    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fd13ezvd6yrslxm.cloudfront.net%2Fwp%2Fwp-content%2Fimages%2Fratatouilleparishuge.jpg&imgrefurl=https%3A%2F%2Fwww.slashfilm.com%2Fnew-ratatouille-movie-trailer-and-photo-still-revealed%2F&docid=JDtew7g33yEc7M&tbnid=Ki-jJYP9pYKudM%3A&vet=10ahUKEwjRuZq1l93mAhWPTsAKHcuMAfcQMwhdKBEwEQ..i&w=2114&h=1028&safe=active&bih=624&biw=656&q=ratatouille%20movie%20trailer&ved=0ahUKEwjRuZq1l93mAhWPTsAKHcuMAfcQMwhdKBEwEQ&iact=mrc&uact=8',
                    'https://www.youtube.com/watch?v=ALUmKa_mpik'
)

movies = [toy_story,avatar,ratatouille,mip]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)