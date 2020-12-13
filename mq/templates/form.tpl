## coding: utf-8
<!DOCTYPE html>
<head>
  <title>Mitarbeiterqualifizierung</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="\hauptansicht.css"/>
</head>
<body>

<header>
  <span style="float:right;">Gruppe / Team angeben</span>
  Mitarbeiterqualifizierung
  <br>
  Version xx / xx.xx.xxxx
</header>

<section>
  <nav>
    <dl>
        <dt><a href="#">Startseite</a></dt>
    <dl>
    <hr>
      <dt><a href="#">Pflege Mitarbeiterdaten</a></dt>
      <dt><a href="#">Pflege Weiterbildungen</a></dt>
    </dl>
    <hr>
    <dl>
      <dt>Teilnahme</dt>
      <dd><a href="#">- Sichtweise Mitarbeiter</a></dd>
      <dd><a href="#">- Sichtweise Weiterbildungen</a></dd>
    </dl>
    <hr>
    <dl>
      <dt>Auswertung</dt>
      <dd><a href="#">- Mitarbeiter</a></dd>
      <dd><a href="#">- Weiterbildungen</a></dd>
      <dd><a href ="#">- Zertifikate</a></dd>
    </dl>
    <hr>
  </nav>
  
  <article>
    <h1>Test</h1>
    <p>Hier steht was schönes</p>
    <p>:)</p>
  </article>
</section>

</body>
</html>## coding: utf-8
<!DOCTYPE html>
<html>
<head>
   <title>Web-Teams</title>
   <meta charset="UTF-8" />
   <link rel="stylesheet" href="\tabelle.css"/>
</head>
<body>
   <form id="idWTForm" action="/save?listform=${listform}" method="POST">
      <input type="hidden" value="${key_s}" id="id_spa" name="id_spa" />
      <div>
         <label for="name1_spa">1. Name</label>
         <input type="text"
                value="${data_o[0]}"
                id="name1_spa"
                name="name1_spa" required />
      </div>
      <div>
         <label for="vorname1_spa">1. Vorname</label>
         <input type="text"
                value="${data_o[1]}"
                id="vorname1_spa"
                name="vorname1_spa" required />
      </div>
      <div>
         <label for="matrnr1_spa">1. Matrikelnummer</label>
         <input type="number"
                value="${data_o[2]}"
                id="matrnr1_spa"
                name="matrnr1_spa" required />
      </div>
      <div>
         <label for="semesternr1_spa">1. Semesternummer</label>
         <input type="number"
                value="${data_o[3]}"
                id="semesternr1_spa"
                name="semesternr1_spa" required />
      </div>
      <div>
         <label for="name2_spa">2. Name</label>
         <input type="text"
                value="${data_o[4]}"
                id="name2_spa"
                name="name2_spa" required />
      </div>
      <div>
         <label for="vorname2_spa">2. Vorname</label>
         <input type="text"
                value="${data_o[5]}"
                id="vorname2_spa"
                name="vorname2_spa" required />
      </div>
      <div>
         <label for="matrnr2_spa">2. Matrikelnummer</label>
         <input type="number"
                value="${data_o[6]}"
                id="matrnr2_spa"
                name="matrnr2_spa" required />
      </div>
      <div>
         <label for="semesternr2_spa">2. Semesternummer</label>
         <input type="number"
                value="${data_o[7]}"
                id="semesternr2_spa"
                name="semesternr2_spa" required />
      </div>
      <br>
      <div>
         <input type="submit" value="Speichern"/>
         <a href="/?listform=${listform}"> Abbrechen </a>
      </div>
   </form>
</body>
</html>
