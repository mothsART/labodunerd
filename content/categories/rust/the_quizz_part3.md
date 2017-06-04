Title: The QuiZz : Partie 3
Category: rust
Tags: rust diesel
Date: 2015-12-11 00:00
Modified: 2015-12-11 00:00
Slug: the-quizz-part-3
Authors: Jérémie Ferry
Status: published
Summary:

## Intro

L'aventure de **The Quizzz** ce poursuis.
Le temps a passé et les objectifs se sont affinés.

Ca m'a permis de tester et promouvoir de nouvelles technos que je vous communiques.

## Utilisation d'un ORM

Comme convenu, on passe à l'étape supérieur avec un ORM digne d'intérêt : [Diesel](http://diesel.rs/) !

    #!sh
    echo DATABASE_URL=postgresql://postgres@localhost > .env

Plus de code passe partout, excepté quand on utilise des routines spécifique à une base de donnée !

Voici les requètes Diesel

    #!rust
    /// Chercher une question aléatoire
    fn get_question(&mut self) -> Question {
        no_arg_sql_function!(random, types::VarChar);
        let query_fragment = questions.limit(1).order(random);
        info!("{:?}", &debug_sql!(query_fragment));
        let b = query_fragment.first(&self.connection).unwrap();
        b
    }
    /// Donner le résultat d'une question filtré par son id
    fn get_response(&mut self, question: Question) -> bool {
        let r = questions.filter(id.eq(question.id)).limit(1).load::<Question>(&self.connection).unwrap();
        info!("{:?}", r[0].response);
        r[0].response
    }


## Frontend 1 : passage de Riot.js à Vue.js

Vue.js est le must du framework web en frontend et mon intérêt va croissant.
(Angular et React ne m'ayant jamais enthousiasmé).

Riot est uniquement orienté composant alors que Vue non.
J'ai été convaincu par : http://sametmax.com/vue-jlavais-pas-vu/

## Frontend 2 : passage de Jquery à Axios et Vanilla

Pour Jquery, c'est une dépendance qui est, à mon sens, de plus en plus inutile.
Pour l'aspect Ajax, j'utiliserais **Axios**.

Axios ne sert qu'à de l'ajax et le fait bien. De plus, il permet des échanges binaires là ou Jquery a bien du mal... (jamais réussi à désérialiser un flux MessagePack)

## Frontend 3 : passage de Twitter Boostrap à Materialize

J'aime beaucoup l'approche de google avec Materialize : donner un cadre précis à l'ergonomie et peaufiner autours.

Le projet est jeune, je n'utilise volontairement que la partie css (le js utilise jquery comme dépendance et ça me semble surfait) mais j'aime vraiment l'idée.

## Backend : passage de Iron à Rocket.rs

Iron est un des tout premier Framework web en Rust.

Son implémentation à débuté bien avant que le langage Rust se stabilise.

Il a par conséquent des soucis d'architecture difficilement réparable et son développement est plus ou moins au point mort.

**[Rocket.rs](https://rocket.rs/)** est un nouveau projet prometteur avec une API simple et fonctionnel.

Une approche proche de Flask (référence à la communauté Python), des exemples à foison etc.

## Utilisation de MessagePack plutôt que Json

MessagePack est à mon goût trop peu connu.
C'est un format de sérialisation binaire compact, avec des outils de sérialisation/désérialisation rapide (bien plus que Json => [mon analyse sur le format](./ce-nest-quun-au-revoir-json.html)) 

Voici un example probant :

code Javascript :

    #!javascript
    function r() {
      axios.post(
        '/r', null,
        {
          responseType: 'blob',
          headers: {'Content-Type': 'application/msgpack; charset=utf-8'}
        }
      ).then(function(response) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var pack = msgpack.decode(new Uint8Array(reader.result));
            console.log(pack);
        }
        reader.readAsArrayBuffer(response.data);
      });
    }

code Rust :

    #!rust
    #[derive(Serialize)]
    pub struct MsgPackResponse {
        pub compact: bool,
        pub schema: i32,
        pub text  : String
    }
    
    #[post("/", format = "application/msgpack")]
    fn r() -> MsgPack<MsgPackResponse> {
        let response = MsgPackResponse {
            compact: true,
            schema :  0,
            text   : "hello msgPack !".to_string()
        };
        MsgPack(response)
    }

## Peaufinement de ma stack

J'ai changé pas mal de détails sur ma [stack](stack-frontend.html) dont nottament le passage à Vue.js...

Néanmoins, je projettes de l'améliorer sensiblement encore dans les mois qui viennent en rajoutant du code Rust et autre.
Le But étant d'avoir un vrai template clé en main pour démarrer un nouveau projet !

## Prochain article

 J'ai pas vraiment décidé qu'elle serait la future piste à explorer mais j'ai plusieurs points qui me sont cher :

### interface en GTK

Et oui, travailler des UI différentes pour le même projet (avec un coeur commn) me parait une bonne idée.

Et puis [GTK.rs](http://gtk-rs.org/) commence à murrir.

### Répétition espacée

Dans le prochain article, je vais me concentrer sur la mise en place d'un algorithme de répétion espacée.
(https://fr.wikipedia.org/wiki/R%C3%A9p%C3%A9tition_espac%C3%A9e)

L'idée derrière cet algo est d'améliorer les connaissances de l'utilisateur en travaillant sur ses faiblesses et non sur ces acquis.

### i18n sur la partie Web
