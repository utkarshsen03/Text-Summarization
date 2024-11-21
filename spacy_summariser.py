import spacy
import pytextrank

nlp = spacy.load('en_core_web_md')


nlp.add_pipe("textrank", last=True)

## TEXT -----
text = "Ferrari (/fəˈrɑːri/; Italian: [ferˈraːri]) is an Italian luxury sports car manufacturer based in Maranello, Italy.\
Founded by Enzo Ferrari in 1939 out of the Alfa Romeo race division as Auto Avio Costruzioni, the company built its first car in 1940. However, the company's inception as an auto manufacturer is usually recognized as 1947, when the first Ferrari-badged car was completed\
Enzo Ferrari was not initially interested in the idea of producing road cars when he formed \
Scuderia Ferrari in 1929, with headquarters in Modena. Scuderia Ferrari (pronounced [skudeˈriːa]) literally means\
\"Ferrari Stable\" and is usually used to mean \"Team Ferrari.\" Ferrari bought,[citation needed] prepared, and \
fielded Alfa Romeo racing cars for gentleman drivers,functioning as the racing division of Alfa Romeo. \
In 1933, Alfa Romeo withdrew its in-house racing team and Scuderia Ferrari took over as its works team:[1]\
the Scuderia received Alfa's Grand Prix cars of the latest specifications and fielded many famous drivers such as Tazio Nuvolari and Achille Varzi.\
In 1938, Alfa Romeo brought its racing operation again in-house, forming Alfa Corse in Milan and hired Enzo Ferrari as manager of the new racing department; therefore the Scuderia Ferrari was disbanded.\
[1]In September 1939, Ferrari left Alfa Romeo under the provision he would not use the Ferrari name in association with races or racing cars for at least four years.[1] \
A few days later he founded Auto Avio Costruzioni, headquartered in the facilities of the old Scuderia Ferrari.[1]\
The new company ostensibly produced machine tools and aircraft accessories. \
In 1940, Ferrari produced a race car – the Tipo 815, based on a Fiat platform. \
It was the first Ferrari car and debuted at the 1940 Mille Miglia, but due to World War II it saw little competition. \
In 1943, the Ferrari factory moved to Maranello, where it has remained ever since. \
The factory was bombed by the Allies and subsequently rebuilt including works for road car production.\
The first Ferrari-badged car was the 1947 125 S, powered by a 1.5 L V12 engine;[1] \
Enzo Ferrari reluctantly built and sold his automobiles to fund Scuderia Ferrari.[15]\
The Scuderia Ferrari name was resurrected to denote the factory racing cars and distinguish them from those fielded by customer teams.\
In 1960 the company was restructured as a public corporation under the name SEFAC S.p.A. (Società Esercizio Fabbriche Automobili e Corse).[16]\
Early in 1969, Fiat took a 50% stake in Ferrari. \
An immediate result was an increase in available investment funds, and work started at once on a factory extension intended to transfer production from Fiat's Turin plant of the Ferrari engined Fiat Dino.\
New model investment further up in the Ferrari range also received a boost.\
In 1988, Enzo Ferrari oversaw the launch of the Ferrari F40, the last new Ferrari launched before his death later that year.\
In 1989, the company was renamed Ferrari S.p.A.[16] \
From 2002 to 2004, Ferrari produced the Enzo, their fastest model at the time, which was introduced and named in honor of the company's founder, Enzo Ferrari. \
It was to be called the F60, continuing on from the F40 and F50, but Ferrari was so pleased with it, they called it the Enzo instead.\
It was initially offered to loyal and recurring customers, each of the 399 made (minus the 400th which was donated to the Vatican for charity) had a price tag of $650,000 apiece (equivalent to £400,900).\
On 15 September 2012, 964 Ferrari cars worth over $162 million (£99.95 million) attended the Ferrari Driving Days event at Silverstone Circuit and paraded round the Silverstone Circuit setting a world record.[17]\
Ferrari's former CEO and Chairman, Luca di Montezemolo, resigned from the company after 23 years, who was succeeded by Amedeo Felisa and finally on 3 May 2016 Amedeo resigned and was succeeded by Sergio Marchionne, CEO and Chairman of Fiat Chrysler Automobiles, Ferrari's parent company.[18]\
In July 2018, Marchionne was replaced by board member Louis Camilleri as CEO and by John Elkann as chairman.[19]\
On 29 October 2014, the FCA group, resulting from the merger between manufacturers Fiat and Chrysler, announced the split of its luxury brand, Ferrari. \
The aim was to turn Ferrari into an independent brand, 10% of whose stake would be sold in an IPO in 2015.[20]\
Ferrari officially priced its initial public offering at $52 a share after the market close on 20 October 2015.[21]"
## TEXT END ---------

doc = nlp(text)

# examine the top-ranked phrases in the document
for p in doc._.phrases:
    print('{:.4f} {:5d}  {}'.format(p.rank, p.count, p.text))
    print(p.chunks)

    
for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=5):
    print(sent)