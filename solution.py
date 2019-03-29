
from operator import itemgetter
import heapq
import collections
def least_common_values(array, to_find=None):
    counter = collections.Counter(array)
    if to_find is None:
        return sorted(counter.items(), key=itemgetter(1), reverse=False)
    return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))

class Slide:
    def __init__(self, isVertical, tags, id):
        self.isVertical = isVertical
        self.tags = tags
        self.id = id

    def __str__(self):
        if self.isVertical:
            return 'Vertical: true, tags: '+str(self.tags)+', id: '+str(self.id)
        else:
            return 'Horitzontal: true, tags: ' + str(self.tags) + ', id: ' + str(self.id)
    def gettags(self):
        return self.tags


def getSlides(file):
    slides = []
    numLinea = -1
    aux = []
    auxFoto=0
    f = open(file)
    lineas = f.readlines()
    multipleVertical = []
    for linea in lineas:
        if numLinea == -1:
              print(linea)
              numLinea += 1
        else:
            numLinea += 1
            lineaArray = linea.split(" ")
            if lineaArray[0] == 'H':
                numberphotos = lineaArray[1]
                tags = []
                for i in range (2, len(lineaArray)):
                    tags.append(lineaArray[i])
                tags[-1] = tags[-1].strip()
                id = [numLinea-1]
                slide = Slide (False, tags, id)
                slides.append(slide)

            elif lineaArray[0] == 'V':
                if len(multipleVertical)==1:
                    numberphotos = lineaArray[1]
                    tags = []
                    for i in range(2, len(lineaArray)):
                        tags.append(lineaArray[i])
                    tagsArray1 = multipleVertical[0].tags
                    tagsArray1[-1] = tagsArray1[-1].strip()
                    tags[-1] = tags[-1].strip()
                    finaltags = set(tagsArray1+tags)
                    id = [multipleVertical[0].id, numLinea-1]
                    slide = Slide(True, finaltags, id)
                    slides.append(slide)
                    multipleVertical.clear()
                elif len(multipleVertical)==0:
                    numberphotos = lineaArray[1]
                    tags = []
                    for i in range(2, len(lineaArray)):
                        tags.append(lineaArray[i])
                    tags[-1] = tags[-1].strip()

                    slide = Slide(True, tags, numLinea-1)
                    multipleVertical.append(slide)
    f.close()
    return slides

def writeOutput(slides, file):
    f = open(file,"a+")
    f.write(str(len(slides))+'\n')
    for slide in slides:
        if len(slide.id) == 2:
            f.write(str(slide.id[0])+' ')
            f.write(str(slide.id[1])+'\n')
        elif len(slide.id)==1:
            f.write(str(slide.id[0])+'\n')
    f.close()



#File to get slides
slides = getSlides("e_shiny_selfies.txt")

slidesfin = []

least_common_ever_id =[]

least_commons = least_common_values(slides)
for least_common in least_commons:
    least_common_ever_id=least_common[0].id

def getLeast_commonI(slidesf):
    least_common_ever_id =[]

    least_commons = least_common_values(slidesf)
    for least_common in least_commons:
        least_common_ever_id=least_common[0].id
    for i in range(len(slidesf)):
        if slidesf[i].id ==least_common_ever_id:
            return i

for i in range(len(slides)):
    if slides[i].id ==least_common_ever_id:
        slidesfin.append(slides[i])
        slides.pop(i)
        break



ranges = len(slides)

for j in range(ranges):
    print((j*100)/(ranges))
    bestslidei = 0
    bestintersact = -1
    for i in range(len(slides)):
        breakFor =False
        intersact=len(set(slides[i].tags) & set(slidesfin[len(slidesfin)-1].tags))
        if i !=0:
            if slides[i].tags == slidesfin[len(slidesfin)-1].tags:
                bestslidei=i
                bestintersact=intersact
                breakFor=True
            elif intersact>=bestintersact:
                if intersact==bestintersact:
                    if len(slides[bestslidei].tags) > len(slides[i].tags):
                        bestslidei=i
                        bestintersact=intersact
                else:
                    bestslidei=i
                    bestintersact=intersact

            elif i == (len(slides)-1) and bestintersact==-1:
                bestslidei=getLeast_commonI(slides)
        if breakFor:
            break
    if len(slides)>=1:
        slidesfin.append(slides[bestslidei])
        slides.pop(bestslidei)
    else:
        break

for slide in slides:
    slidesfin.append(slide)


slides = slidesfin


#Output File
writeOutput(slides, "outputE_append.txt")


for slide in slides:
    print(slide)
