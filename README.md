# JSBlog

Mini blog créé avec Python et le célèbre Framework web Django.

**Installation & utilisation**


<aside>
💡 Petit disclaimer, 
pour installer le projet chez vous de manière confortable, soyez sûr d'être à l'aise avec les environnements Python, Django et autres… Car cet didacticiel n'entre dans aucun details techniques.

Aussi la méthode d’installation proposée est celle qui marche pour Windows. Alors n’hésitez pas à faire quelques recherches pour trouver l’équivalent si vous êtes sur un autre système.

</aside>

- Ouvrez un nouveau terminal et clonez le repo chez vous:
    
    ```bash
    git clone <lien du repo>
    ```
    
    Assurez-vous d'avoir git d'installé sur votre machine
    
- Un nouveau dossier sera créé dans le répertoire courant (JSBlog). Rendez-vous à l’intérieur avec la syntaxe:
    
    ```bash
    cd .\JSBlog
    ```
    
- Créer un nouvel environnement virtuel python
    
    ```bash
    python -m venv env
    ```
    
- Activez l’environnement virtuel
    
    ```bash
    .\env\Script\activate
    ```
    
- Installez les dépendances du projet avec cette syntaxe
    
    ```bash
    pip install -r requirements.txt
    ```
    

Vous êtes maintenant prêt à manipuler l'environnement Django.

- Effectuer les différentes migrations vers la base de donnée
    
    ```powershell
    py .\src\manage.py migrate
    ```
    
- Lancer le serveur local
    
    ```powershell
    py .\src\manage.py runserver
    ```
    

Ça y est, vous êtes maintenant en mesure d’explorer l’app JSBlog. Vous avez juste qu'à visiter l’url du serveur local ‘[http://localhost:8000/](http://localhost:8000/)’ ou ‘[http://127.0.0.1:8000/](http://127.0.0.1:8000/)’ .

![image](https://user-images.githubusercontent.com/97140632/215323377-4b9140f6-2456-4fe6-a3bb-a7f076fbd6d0.png)

<aside>
💡 Il faut savoir que je n'ai pas voulu surcharger le repo en ajoutant le fichier de la base de données. Alors, de base, il n'y aura rien d'affiché sur le blog, puisque la nouvelle base de données générée chez vous ne contiendra rien du tout.

Pour remédier à ce problème, j'ai mis en place une commande pour générer du faux contenu déjà préconçu.

</aside>

Arrêter le serveur avec ‘ctrl c’ et exécutez la commande ‘**collectedatas**’:

```bash
py .\src\manage.py collectedatas
```

Relancez le serveur local et revisitez le site, vous constaterai un changement.  

![image](https://user-images.githubusercontent.com/97140632/215323442-6e3c826f-4347-4095-a8e7-1ae1b31e1e3f.png)

Pour ajouter du contenu personnalisé et d’une manière plus graphique, accéder a linterface d'administration de l’app. Pour ce faire devez créer ce qu’on appel un super user. Arrêtez encore une fois le serveur et procédez de la manière suivante:

```powershell
py .\src\manage.py createsuperuser
```

Surviendra différents prompts, entrez les infos nécessaires pour valider la création du super user. 

Relancez le [localhost](http://localhost) et accédez à l'url ‘[http://127.0.0.1:8000/](http://127.0.0.1:8000/)jsb-admin149/’, 

![image](https://user-images.githubusercontent.com/97140632/215323463-e94c74b9-f875-4bdf-be7c-2bab410375d4.png)

Authentifiez-vous avec vos infos et accéder a linterface d'administration.

![image](https://user-images.githubusercontent.com/97140632/215323483-e4c1f1aa-7594-46b2-b91c-8842a7e366a7.png)

Commencer à administrer le site comme bon vous semble.

![image](https://user-images.githubusercontent.com/97140632/215323502-702db25f-6327-481f-a6a8-06224f65a5cc.png)

De plus, après connexion vous constaterai de retour sur le site, que les articles y seront directement modifiable.

![image](https://user-images.githubusercontent.com/97140632/215323515-28868581-7f5d-44fc-a2d7-4efb741f4c0f.png)

Vous pourrai donc créer, modifier et supprimer du contenu directement sur le blog.
