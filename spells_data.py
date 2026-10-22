"""Transcriptions de démonstration relues sur les scans des pages 242-247.
Les textes sont des données distinctes des scripts de génération.
"""
SPELLS=[]

def add(name, school, level, classes, casting, range_, comps, duration, pages, body, *, illustration=None, illustration_caption=None, notes=None):
    SPELLS.append(dict(nom=name, ecole=school, niveau=level, classes=classes,
        incantation=casting, portee=range_, composantes=comps, duree=duration,
        pages_source=pages, description=body.strip(), illustration=illustration,
        legende_illustration=illustration_caption, notes_verification=notes or '',
        statut='transcription_revue_visuellement'))

add('Appel de destrier','Invocation',2,['Paladin'],'action','9 m','V, S','instantanée',[242],'''
Vous convoquez un être d'outre-monde qui se présente comme une monture fidèle en un espace inoccupé que vous choisissez à portée. Cette créature reprend le profil de la **monture d'outre-monde**. Si vous disposez déjà d'une telle monture par le biais de ce sort, elle est remplacée par la nouvelle.

Vous choisissez l'aspect de votre monture, un animal que l'on peut monter de taille G, comme un cheval, un chameau, un loup sanguinaire ou un grand cervidé. Chaque fois que vous lancez le sort, choisissez le type de créature de la monture : Céleste, Fée ou Fiélon, qui détermine certains traits du profil.

**Combat.** La monture constitue un allié pour vous et vos alliés. Au combat, elle partage votre rang d'Initiative et se gère comme une monture contrôlée lorsque vous la chevauchez (comme décrit dans les règles du combat monté). Si vous subissez l'état Neutralisé, la monture joue son tour juste après vous et agit de manière autonome en veillant à vous protéger.

**Disparition de la monture.** La monture disparaît si elle tombe à 0 point de vie ou si vous mourez. À sa disparition, elle laisse derrière elle tout ce qu'elle portait. Si vous relancez ce sort, vous décidez si vous convoquez la monture disparue ou une autre.

**Emplacement de niveau supérieur.** Le niveau de l'emplacement s'applique chaque fois que le profil de jeu y fait référence.

## Monture d'outre-monde

*Céleste, Fée ou Fiélon (à votre convenance) de taille G, Neutre*

**CA** 10 + 1 par niveau du sort  
**PV** 5 + 10 par niveau du sort (la monture dispose d'un nombre de DV [d10] égal au niveau du sort)  
**Vitesse** 18 m, vol 18 m (sort du 4e niveau ou plus)

| Caractéristique | Valeur | Mod. | JS |
|:---|---:|---:|---:|
| FOR | 18 | +4 | +4 |
| DEX | 12 | +1 | +1 |
| CON | 14 | +2 | +2 |
| INT | 6 | −2 | −2 |
| SAG | 12 | +1 | +1 |
| CHA | 8 | −1 | −1 |

**Sens** Perception passive 11  
**Langues** télépathie 1,5 km (fonctionne uniquement avec vous)  
**FP** aucun (PX 0 ; BM égal à votre bonus de maîtrise)

### Traits

**Lien vital.** Lorsque vous récupérez des points de vie par un sort du 1er niveau ou supérieur, la monture en récupère autant si vous vous trouvez à 1,50 m ou moins d'elle.

### Actions

**Coup d'outre-monde.** *Corps à corps* : bonus égal à votre modificateur d'attaque des sorts, allonge 1,50 m. *Touché* : 1d8 plus niveau du sort dégâts radiants (Céleste), psychiques (Fée) ou nécrotiques (Fiélon).

### Actions Bonus

**Contact guérisseur (Céleste uniquement ; recharge après un Repos long).** Une créature dans un rayon de 1,50 m de la monture récupère un nombre de points de vie égal à 2d8 + niveau du sort.

**Foulée féerique (Fée uniquement ; recharge après un Repos long).** La monture se téléporte avec son cavalier en un espace inoccupé de votre choix dans un rayon de 18 m.

**Regard fiélon (Fiélon uniquement ; recharge après un Repos long).** JS Sagesse : votre DD de sauvegarde des sorts, une créature dans un rayon de 18 m que la monture voit. *Échec* : la cible subit l'état Effrayé jusqu'à la fin de votre tour suivant.
''')

add('Appel de familier','Invocation',1,['Magicien'],'1 heure ou rituel','3 m',"V, S, M (de l'encens qui brûle d'une valeur minimale de 10 po, que le sort détruit)",'instantanée',[242,243],'''
Vous recevez les services d'un familier, esprit qui prend la forme animale de votre choix : **araignée, belette, chat, chauve-souris, chouette, corbeau, faucon, grenouille, lézard, pieuvre, rat** ou autre Bête dont le facteur de puissance est de 0. Le familier se présente en un espace inoccupé à portée, avec le profil de jeu de la forme retenue (cf. annexe B), si ce n'est qu'il s'agit d'un Céleste, d'une Fée ou d'un Fiélon (à votre convenance) et non d'une Bête. Votre familier agit indépendamment de vous, mais il obéit à vos instructions.

**Lien télépathique.** Tant que votre familier se trouve dans un rayon de 30 m de vous, vous pouvez communiquer avec lui par télépathie. De plus, par une action Bonus, vous pouvez voir par ses yeux et entendre par son ouïe jusqu'au début de votre tour suivant, en bénéficiant de ses éventuels sens spéciaux.

Enfin, si vous lancez un sort dont la portée est « contact », votre familier peut appliquer ce contact. Il doit se trouver dans un rayon de 30 m de vous et doit jouer sa Réaction pour appliquer le contact lors de l'incantation.

**Combat.** Le familier est votre allié, ainsi que celui de vos alliés. Il joue sa propre Initiative et agit à son tour. Un familier ne peut pas attaquer, mais il peut entreprendre normalement d'autres actions.

**Disparition du familier.** Quand le familier tombe à 0 point de vie, il disparaît. Il réapparaît si vous relancez ce sort. Au prix de l'action Magie, vous pouvez provisoirement révoquer le familier dans une niche dimensionnelle. Vous pouvez également le révoquer à tout jamais. Au prix de l'action Magie, tant qu'il est provisoirement révoqué, vous pouvez le faire réapparaître en un espace inoccupé dans un rayon de 9 m de vous. Quand le familier tombe à 0 point de vie ou disparaît dans une niche dimensionnelle, il laisse tout ce qu'il porte sur lui dans son espace.

**Un seul familier.** Vous ne pouvez pas disposer de plus d'un familier à la fois. Si vous lancez ce sort alors que vous disposez déjà d'un familier, ce dernier adopte en fait une nouvelle forme adaptée.
''', illustration='familiers.jpg', illustration_caption="Les formes des esprits convoqués par Appel de familier s'inspirent des mages qui les invoquent.")

add('Appel de la foudre','Invocation',3,['Druide'],'action','36 m','V, S',"Concentration, jusqu'à 10 minutes",[243],'''
Un nuage menaçant se présente en un point que vous voyez à portée et qui vous surplombe directement. Il prend la forme d'un Cylindre haut de 3 m pour un rayon de 18 m.

À l'incantation du sort, choisissez un point que vous voyez sous le nuage. Un trait de foudre jaillit du nuage vers ce point. Chaque créature située dans un rayon de 1,50 m de ce point effectue un jet de sauvegarde de Dextérité et subit 3d10 dégâts de foudre en cas d'échec, la moitié en cas de réussite.

Jusqu'à la fin du sort, vous pouvez entreprendre l'action Magie pour invoquer chaque fois un nouvel éclair, en ciblant le même point ou un autre.

Si vous êtes en extérieur et en conditions orageuses à l'incantation du sort, il vous donne le contrôle de l'orage en cours au lieu d'en créer un. Dans de telles conditions, les dégâts du sort augmentent de 1d10.

**Emplacement de niveau supérieur.** Les dégâts augmentent de 1d10 par niveau d'emplacement au-delà du 3e.
''')

add('Arme élémentaire','Transmutation',3,['Druide','Paladin','Rôdeur'],'action','contact','V, S',"Concentration, jusqu'à 1 heure",[243],'''
Une arme non magique que vous touchez devient magique. Choisissez un type de dégâts parmi les suivants : acide, feu, foudre, froid et tonnerre. Pour toute la durée, l'arme dispose d'un bonus de +1 aux jets d'attaque et inflige 1d4 dégâts supplémentaires du type choisi en cas de réussite.

**Emplacement de niveau supérieur.** Avec un emplacement du 5e ou 6e niveau, le bonus aux jets d'attaque passe à +2 et les dégâts supplémentaires à 2d4. Avec un emplacement du 7e niveau ou supérieur, le bonus passe à +3 et les dégâts supplémentaires à 3d4.
''')

add('Arme magique','Transmutation',2,['Ensorceleur','Magicien','Paladin','Rôdeur'],'action Bonus','contact','V, S','1 heure',[244],'''
Vous touchez une arme non magique. Jusqu'à la fin du sort, l'arme devient magique, dotée d'un bonus de +1 aux jets d'attaque et aux jets de dégâts. Le sort prend fin prématurément si vous le lancez à nouveau.

**Emplacement de niveau supérieur.** Le bonus passe à +2 avec un emplacement du 3e, 4e ou 5e niveau. Le bonus passe à +3 avec un emplacement du 6e niveau ou supérieur.
''')

add('Arme spirituelle','Évocation',2,['Clerc'],'action Bonus','18 m','V, S',"Concentration, jusqu'à 1 minute",[244],'''
Vous créez une arme spectrale et flottante à l'image de l'arme de votre choix, qui persiste pour toute la durée. L'arme apparaît à portée dans l'espace de votre choix et vous pouvez aussitôt effectuer une attaque de sort au corps à corps contre une créature située dans un rayon de 1,50 m de l'arme. Si l'attaque touche, la cible subit des dégâts de force égaux à 1d8 + votre modificateur de caractéristique d'incantation.

Par une action Bonus à chaque tour consécutif, vous pouvez déplacer l'arme d'un maximum de 6 m et répéter l'attaque contre une créature située dans un rayon de 1,50 m de l'arme.

**Emplacement de niveau supérieur.** Les dégâts augmentent de 1d8 par niveau d'emplacement au-delà du 2e.
''',illustration='arme-spirituelle.jpg',illustration_caption='Un clerc goliath lance arme spirituelle face à un mastodonte des ombres.')

add("Armure d’Agathys",'Abjuration',1,['Occultiste'],'action Bonus','personnelle','V, S, M (un éclat de verre bleu)','1 heure',[245],'''
Un givre magique protecteur vous enveloppe. Vous recevez 5 points de vie temporaires. Si une créature vous touche avec un jet d'attaque de corps à corps avant la fin du sort, elle subit 5 dégâts de froid. Le sort prend fin prématurément si vous n'avez plus de points de vie temporaires.

**Emplacement de niveau supérieur.** Les points de vie temporaires et les dégâts de froid augmentent de 5 par niveau d'emplacement au-delà du 1er.
''')

add('Armure du mage','Abjuration',1,['Ensorceleur','Magicien'],'action','contact','V, S, M (un morceau de cuir traité)','8 heures',[245],'''
Vous touchez une créature consentante qui ne porte pas d'armure. Jusqu'à la fin du sort, sa CA de base est de 13 plus son modificateur de Dextérité. Le sort prend fin prématurément si la cible enfile une armure.
''',illustration='armure-du-mage.jpg',illustration_caption='Un magicien humain pare au danger grâce à armure du mage et aux traits infaillibles de projectile magique.')

add('Arrêt du temps','Transmutation',9,['Ensorceleur','Magicien'],'action','personnelle','V','instantanée',[245],'''
Vous mettez un bref coup d'arrêt à l'écoulement du temps, pour tout le monde sauf vous-même. Le temps s'arrête pour les autres créatures tandis que vous prenez 1d4 + 1 tours d'affilée, durant lesquels vous pouvez entreprendre des actions et vous déplacer comme en temps normal.

Ce sort prend fin si l'une des actions que vous entreprenez durant l'intervalle, ou l'un des effets créés, affecte une créature autre que vous ou un objet porté par quelqu'un d'autre que vous. Il se termine également si vous vous déplacez en un lieu distant de plus de 300 m de l'endroit où vous l'avez lancé.
''')

add('Aspersion acide','Évocation',0,['Ensorceleur','Magicien'],'action','18 m','V, S','instantanée',[246],'''
Vous créez une bulle acide en un point à portée, où elle explose sous forme de Sphère de 1,50 m de rayon. Chaque créature prise dans la Sphère doit réussir un jet de sauvegarde de Dextérité sous peine de subir 1d6 dégâts d'acide.

**Amélioration de sort mineur.** Les dégâts augmentent de 1d6 lorsque vous atteignez les niveaux 5 (2d6), 11 (3d6) et 17 (4d6).
''')

add('Assassin imaginaire','Illusion',4,['Barde','Magicien'],'action','36 m','V, S',"Concentration, jusqu'à 1 minute",[246],'''
Vous puisez dans les cauchemars d'une créature que vous voyez à portée pour créer une illusion de ses plus grandes craintes, visible uniquement de la créature. La cible effectue un jet de sauvegarde de Sagesse. En cas d'échec, la cible subit 4d10 dégâts psychiques, ainsi que le Désavantage aux tests de caractéristique et aux jets d'attaque pour toute la durée. En cas de réussite, la cible subit la moitié de ces dégâts et le sort prend fin.

Pour toute la durée, la cible peut effectuer un JS Sagesse à la fin de chacun de ses tours. En cas d'échec, elle subit de nouveau les dégâts psychiques. En cas de réussite, le sort prend fin.

**Emplacement de niveau supérieur.** Les dégâts augmentent de 1d10 par niveau d'emplacement au-delà du 4e.
''')

add('Assistance','Divination',0,['Clerc','Druide'],'action','contact','V, S',"Concentration, jusqu'à 1 minute",[246],'''
Vous touchez physiquement une créature consentante en choisissant une compétence. Jusqu'à la fin du sort, la créature ajoute 1d4 au résultat de tout test de caractéristique associé à cette compétence.
''')

add('Augure','Divination',2,['Clerc','Druide','Magicien'],'1 minute ou rituel','personnelle','V, S, M (cartes, os ou bâtonnets gravés spécialement, ou objets divinatoires comparables, d’une valeur minimale de 25 po)','instantanée',[246],'''
Vous recevez un présage d'une entité surnaturelle vous renseignant sur l'issue d'une opération que vous comptez mener dans les 30 minutes. Le MD choisit une option de la table Présages :

### Présages

| Présage | Pour une issue qui s'annonce… |
|:---|:---|
| Fortune | favorable |
| Misère | défavorable |
| Fortune et misère | favorable et défavorable |
| Indifférence | ni favorable ni défavorable |

Le sort ne tient pas compte des conjonctures qui pourraient peser dans la balance, comme l'incantation de nouveaux sorts.

Si vous lancez le sort plus d'une fois avant de terminer votre prochain Repos long, vous courez dès la deuxième incantation 25 % de risques cumulatifs qu'il ne vous livre aucune réponse.
''')

add('Aura du croisé','Évocation',3,['Paladin'],'action','personnelle','V',"Concentration, jusqu'à 1 minute",[246],'''
Vous produisez une aura magique sous forme d'une Émanation de 9 m. Toute créature alliée comprise dans l'aura (y compris vous) inflige 1d4 dégâts radiants supplémentaires lorsqu'elle touche avec une arme ou une attaque à mains nues.
''')

add('Aura magique de Nystul','Illusion',2,['Magicien'],'action','contact','V, S, M (un petit carré de soie)','24 heures',[246,247],'''
D'un contact, vous placez une illusion sur une créature consentante ou un objet qui n'est porté par personne. Une créature reçoit l'effet Masque, tandis qu'un objet reçoit l'effet Aura factice (voir plus loin). Les effets persistent pour toute la durée. Si vous lancez ce sort sur une même créature ou un même objet pendant 30 jours consécutifs, l'illusion persiste jusqu'à dissipation.

**Masque (créature).** Choisissez un type de créature autre que celui de la cible. Les sorts et effets magiques considèrent désormais la cible comme du type retenu.

**Aura factice (objet).** Vous altérez la manière dont la cible se dévoile au gré de sorts et effets magiques qui perçoivent les auras magiques, tels que *détection de la magie*. Vous pouvez ainsi faire qu'un objet ordinaire paraisse magique, qu'un objet magique paraisse ordinaire, ou modifier l'aura magique d'un objet pour qu'elle soit associée à l'école de magie de votre choix.
''')
