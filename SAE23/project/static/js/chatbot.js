// Liste des questions et réponses
const questionsReponses = [
    {
      question: "Help",
      reponse: "Voici la liste des questions que vous pouvez me poser : \n Comment ajouter une machine \n Comment ajouter un personnel \n Comment se connecter \n Comment supprimer une machine \n Comment supprimer un personnel \n Pourquoi je ne peux ni supprimer ni ajouter \n Identifiant admin"
    },
    {
      question: "Comment ajouter une machine",
      reponse: "Il vous suffit d'accèder à la page 'Ajouter des machines et du personnel' depuis la page d'accueil, puis de séléctionner 'Ajouter une machine'."
    },
    {
        question: "Comment ajouter un personnel",
        reponse: "Il vous suffit d'accèder à la page 'Ajouter des machines et du personnel' depuis la page d'accueil, puis de séléctionner 'Ajouter un personnel'."
    },
    {
        question: "Comment supprimer une machine",
        reponse: "Pour supprimer une machine il vous faut accèder à la page spécifique de la machine en cliquant sur son ID dans la liste des machines."
    },
    {
        question: "Comment supprimer un personnel",
        reponse: "Pour supprimer un personnel il vous faut accèder à la page spécifique du personnel en cliquant sur son ID dans la liste des personnels."
    },
    {
        question: "Comment se connecter",
        reponse: "La page de connexion est accessible en cliquant sur l'icon profile dans la page d'accueil."
    },
    {
        question: "Pourquoi je ne peux ni supprimer ni ajouter",
        reponse: "Par mesure de protection, seul un administrateur peut le faire, il faut donc être connecté au compte admin."
    },
    {
        question: "Identifiant admin",
        reponse: "Username : admin | Password : gtrnet"
    },
    // Ajoutez d'autres paires question/réponse ici
  ];
  
  // Fonction pour obtenir une réponse à partir d'une question
  function obtenirReponse(question) {
    // Recherche de la question dans la liste
    const questionReponse = questionsReponses.find(qr => qr.question.toLowerCase() === question.toLowerCase());
  
    // Retourne la réponse correspondante ou un message par défaut si la question n'est pas trouvée
    return questionReponse ? questionReponse.reponse : "Désolé, je ne comprends pas. Pouvez-vous reformuler votre question ? Ou utilisez la commande 'Help' pour afficher les commandes disponible.";
  }
  
  // Fonction pour traiter les messages de l'utilisateur
  function traiterMessage() {
    const userInput = document.getElementById('userinput').value;
    const chatbox = document.getElementById('chatbox');
  
    // Création de l'élément de message de l'utilisateur
    const userMessage = document.createElement('p');
    userMessage.className = 'user-message';
    userMessage.innerText = 'Utilisateur : ' + userInput;
  
    // Création de l'élément de message du chatbot
    const chatbotMessage = document.createElement('p');
    chatbotMessage.className = 'chatbot-message';
    chatbotMessage.innerText = 'Chatbot : ' + obtenirReponse(userInput);
  
    // Ajout des messages à la zone de chat
    chatbox.appendChild(userMessage);
    chatbox.appendChild(chatbotMessage);
  
    // Effacement du champ de saisie de l'utilisateur
    document.getElementById('userinput').value = '';
  }
  