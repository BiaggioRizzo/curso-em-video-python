# Exercício Conversão de medidas

distancia = int(input('Digite uma distância em metros: '))

multiplicador = 10
dam = distancia / multiplicador
hm = dam / multiplicador
km = hm / multiplicador
dm = distancia * multiplicador
cm = multiplicador * dm
mm = multiplicador * cm

print("km:  {} km\nhm:  {} hm\ndam: {} dam\n"
      "m:   {} m\ndm:  {} dm\ncm:  {} cm\nmm:  {} mm".format(km, hm, dam, distancia, dm, cm, mm))

