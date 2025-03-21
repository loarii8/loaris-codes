import time
import os

def pastrimi_i_ekranit():
    """Pastro ekranin për të simuluar një skenë të re."""
    os.system('cls' if os.name == 'nt' else 'clear')

def printo_ngadalë(str, vonesë=0.05):
    """Printon tekstin ngadalë, shkronjë për shkronjë."""
    for shkronjë in str:
        print(shkronjë, end='', flush=True)
        time.sleep(vonesë)
    print()

def printo_visuale(skena):
    """Printon një pamje ASCII në bazë të skenës."""
    pamjet = {
        "fillim": """
        =========================================
        | Mirësevini në Aventurën e Madhe!      |
        =========================================
            Udhëtimi juaj fillon këtu...
        """,
        "rruga_krejt": """
        Hyni në një pyll të dendur...
           ,     ,
         ( o )-( o )
           `----'
        Pemët janë të dendura, ajri është i ftohtë.
        Dëgjoni fërshëllimën e gjetheve...
        """,
        "rruga_djathtas": """
        Hyni në një shpellë të errët...
         _______
        /       \\
       |   o o   |
        \\_______/
        Më shijon një erë e lagur.
        Dëgjoni diçka që pikëllon brenda...
        """,
        "rruga_përpara": """
        Hyni në një fushë të gjelbër...
        \\    /\\
         )  ( ')
        (  /  )
         \\(__)|
        Dëgjoni zhurmën e ujit që rrjedh...
        """,
        "pasuri": """
        Gjetët një arkë të fshehtë thesari!
        _  _  _  _  _
       | | | | | | | |
       | | | | | | | |
       |_|_|_|_|_|_|_|
        Brenda gjeni 50 copa ari!
        """,
        "dragua": """
        Një dragua e egër shfaqet!
             __====-_  _-====___
        _--^^^#####//      \\#####^^^--_
       -^##########// (    ) \\##########^-_
      _/##########//  |\^^/|  \\##########\_
     /##########//   (@::@)   \\##########\_
    -^##########//     \\//     \\##########^-_
   -############//       ( )       \\############^-_
  _/##########//         ( )         \\##########\_
 /##########//           ( )           \\##########\_
-^##########//            ( )            \\##########^-_
        """,
        "magjistari": """
        Një magjistar i mençur shfaqet!
              _____
            .-'     `-.
           /         \\
          |           |
          |   O   O   |
           \\   (_)   /
            `-._____.-'
        Magjistari ju jep një magji zjarri!
        """,
        "liqeni": """
        Hyni në një liqen të qetë...
             ____
          .-'    `-.
        .-'          `-.
       /                \\
      |    _______      |
       \\  /       \\    /
        `'         `-''
        Dëgjoni zhurmën e ujit që rrjedh...
        """,
        "hendek": """
        Hyni në një hendek të thellë...
        _______
       /       \\
      |   O O   |
       \\_______/
        Ju rrëzoheni dhe humbni shëndet!
        """
    }
    printo_ngadalë(pamjet.get(skena, ""))

def zgjedh_aksion():
    """Përgjigje për zgjedhjen e një veprimi."""
    printo_ngadalë("Keni tre rrugë para jush.")
    printo_ngadalë("A doni të shkoni majtas, djathtas apo përpara?")
    zgjedhja = input("Shkruani 'majtas', 'djathtas' ose 'përpara': ").lower()
    return zgjedhja

def ngjarje_rrugës(rruga, shëndeti, ari, magji):
    """Kthen një ngjarje të caktuar për çdo rrugë."""
    if rruga == 'majtas':
        if not magji:
            printo_visuale("magjistari")
            printo_ngadalë("Takoni një magjistar të mençur që ju dhuron një magji zjarri!")
            magji.append("Zjarri")
        else:
            printo_visuale("dragua")
            printo_ngadalë("Një dragua e egër shfaqet! Ai rënkon, por arrini të shpëtoni.")
            shëndeti -= 10
    elif rruga == 'djathtas':
        if ari < 100:
            printo_visuale("pasuri")
            printo_ngadalë("Gjetët një arkë të fshehtë thesari! Keni fituar 50 ari.")
            ari += 50
        else:
            printo_visuale("hendek")
            printo_ngadalë("Hyni në një hendek dhe humbni disa pikë shëndeti. Jini më të kujdesshëm!")
            shëndeti -= 20
    else:
        if shëndeti < 80:
            printo_visuale("liqeni")
            printo_ngadalë("Gjetët një liqen të qetë dhe u pini ujë të freskët. Shëndeti juaj u rrit.")
            shëndeti += 10
        else:
            printo_visuale("dragua")
            printo_ngadalë("Një dragua e egër shfaqet! Ai rënkon, por arrini të shpëtoni.")
            shëndeti -= 10
    return shëndeti, ari, magji

def loja_aventura():
    """Funksioni kryesor i lojës."""
    pastrimi_i_ekranit()
    printo_visuale("fillim")
    shëndeti = 100
    ari = 0
    magji = []

    while shëndeti > 0:
        # Merrni zgjedhjen e përdoruesit
        aksioni = zgjedh_aksion()
        pastrimi_i_ekranit()

        # Shfaq pamjen në bazë të rrugës të zgjedhur
        if aksioni == 'majtas':
            printo_visuale("rruga_krejt")
        elif aksioni == 'djathtas':
            printo_visuale("rruga_djathtas")
        else:
            printo_visuale("rruga_përpara")

        # Ngjarja e caktuar për çdo rrugë
        shëndeti, ari, magji = ngjarje_rrugës(aksioni, shëndeti, ari, magji)

        # Shfaq statusin aktual
        printo_ngadalë(f"Shëndeti aktual: {shëndeti} | Ari: {ari} | Magjitë: {magji}")

        # Kontrolloni nëse shëndeti bie në zero ose më poshtë
        if shëndeti <= 0:
            printo_ngadalë("Keni humbur të gjithë shëndetin tuaj. Loja ka mbaruar!")
            break

        # Pyetni nëse lojtari dëshiron të vazhdojë ose jo
        vazhdo_lojën = input("Doni të vazhdoni aventurën? (po/jo): ").lower()
        if vazhdo_lojën != 'po':
            printo_ngadalë("Faleminderit që luajtët! Mirupafshim.")
            break

if __name__ == "__main__":
    loja_aventura()
