(ns tracks-on-tracks-on-tracks)

(defn new-list []
  "Creates an empty list of languages to practice."
  (list))

(defn add-language [lang-list lang]
  "Adds a language to the list."
  (cons lang lang-list))

(defn first-language [lang-list]
  "Returns the first language on the list."
  (first lang-list))

(defn remove-language [lang-list]
  "Removes the first language added to the list."
  (rest lang-list))

(defn count-languages [lang-list]
  "Returns the total number of languages on the list."
  (count lang-list))

(defn learning-list []
  "Creates an empty list, adds Clojure and Lisp, removes Lisp, adds
  Java and JavaScript, then finally returns a count of the total number
  of languages."
(-> (new-list)
    (add-language "Clojure")
    (add-language "Lisp")
    (remove-language)
    (add-language "Java")
    (add-language "JavaScript")
    (count-languages)))
