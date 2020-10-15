<template>
  <v-container fluid justify-center>
    <v-form ref="form">

      <v-layout row wrap justify-center mb-8>
        <v-flex xs12 md6 lg4>
          <v-text-field label="Name" v-model="name" :rules="inputRequiredRule"></v-text-field>
        </v-flex>
      </v-layout>

      <h1 class="mb-4">Youtube</h1>
      <div>Select up to 5 of your favourite Youtube video categories</div>
      <div id="youtubeCategory">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete v-model="youtubeCategory" :items="inputYoutube" label="Category">
            </v-autocomplete>
          </v-flex>
        </v-layout>
        <div class="mb-4">Drag to Rank</div>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="1"> Most Favourite </v-col>
          <v-col cols="6">
            <v-card style="padding-left: 10px" max-width="700" class="mx-auto">
              <v-card-text style="align-items:center">
                <v-chip-group v-model="youtubeSelection" column active-class="primary--text">
                  <draggable v-model="youtubes" @start="dragStartYoutube" @end="dragEndYoutube">
                    <v-chip v-for="(y, i) in youtubes" :key="i" draggable>{{
                      y
                    }}</v-chip>
                  </draggable>
                </v-chip-group>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="1"> Least Favourite </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </div>

      <div class="mb-12"></div>

      <h1 class="mb-4">Books</h1>
      <div>Select up to 5 of your favourite book subjects</div>

      <div id="book">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete v-model="bookGenre" :items="inputBook" label="Genre">
            </v-autocomplete>
          </v-flex>
        </v-layout>
        <div class="mb-4">Drag to Rank</div>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="1"> Most Favourite </v-col>
          <v-col cols="6">
            <v-card style="padding-left: 10px" max-width="700" class="mx-auto">
              <v-card-text>
                <v-chip-group v-model="bookGenre" column active-class="primary--text">
                  <draggable v-model="bookGenre" @start="dragStartBook" @end="dragEndBook">
                    <v-chip v-for="(tag, i) in books" :key="i" draggable>{{
                      tag
                    }}</v-chip>
                  </draggable>
                </v-chip-group>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="1"> Least Favourite </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </div>

      <div class="mb-12"></div>

      <h1 class="mb-4">Movies</h1>
      <div>Select up to 5 of your favourite movie genres</div>

      <div id="movieGenre">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete v-model="movieGenre" :items="inputMovieGenre" label="Genre">
            </v-autocomplete>
          </v-flex>
        </v-layout>
        <div class="mb-4">Drag to Rank</div>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="1"> Most Favourite </v-col>
          <v-col cols="6">
            <v-card style="padding-left: 10px" max-width="700" class="mx-auto">
              <v-card-text>
                <v-chip-group v-model="movieGenre" column active-class="primary--text">
                  <draggable v-model="movieGenre" @start="dragStartMovie" @end="dragEndMovie">
                    <v-chip v-for="(m, i) in movies" :key="i" draggable>{{
                      m
                    }}</v-chip>
                  </draggable>
                </v-chip-group>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="1"> Least Favourite </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </div>

      <div class="mb-12"></div>

      <v-layout row wrap justify-center mb-8>
        <v-flex xs12 md6 lg4>
          <div>List your preferred languages</div>
          <v-autocomplete v-model="movieLanguage" :items="inputMovieLang" label="Language" multiple chips deletable-chips :rules="inputRequiredRule"></v-autocomplete>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-center mb-8>
        <v-flex xs12 md6 lg4>
          <div>Pick a minimum IMDB value</div>
          <v-slider v-model="movieImdb" :max="10" :min="0" :step="0.1" :thumb-size="30" thumb-label mb-8></v-slider>
        </v-flex>
      </v-layout>

      <h1 class="mb-4">Spotify</h1>
      <div>Select up to 3 of your favourite artists</div>
      <div id="spotifyArtist">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete v-model="spotifyArtist" :items="inputSpotifyArtist" label="Artist">
            </v-autocomplete>
          </v-flex>
        </v-layout>
        <div class="mb-4">Drag to Rank</div>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="1"> Most Favourite </v-col>
          <v-col cols="6">
            <v-card style="padding-left: 10px" max-width="700" class="mx-auto">
              <v-card-text>
                <v-chip-group v-model="spotifyArtist" column active-class="primary--text">
                  <draggable v-model="spotifyArtist" @start="dragStartSArtist" @end="dragEndSArtist">
                    <v-chip v-for="(tag, i) in sArtists" :key="i" draggable>{{
                      tag
                    }}</v-chip>
                  </draggable>
                </v-chip-group>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="1"> Least Favourite </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </div>

      <div class="mb-12"></div>

      <div class="mb-8"></div>
      <div>Select up to 3 of your favourite tracks</div>
      <div id="spotifyTrack">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete v-model="spotifyTrack" :items="inputSpotifyTrack" label="Track">
            </v-autocomplete>
          </v-flex>
        </v-layout>
        <div class="mb-4">Drag to Rank</div>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="1"> Most Favourite </v-col>
          <v-col cols="6">
            <v-card style="padding-left: 10px" max-width="700" class="mx-auto">
              <v-card-text>
                <v-chip-group v-model="spotifyTrack" column active-class="primary--text">
                  <draggable v-model="spotifyTrack" @start="dragStartSTrack" @end="dragEndSTrack">
                    <v-chip v-for="(tag, i) in sTracks" :key="i" draggable>{{
                      tag
                    }}</v-chip>
                  </draggable>
                </v-chip-group>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="1"> Least Favourite </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </div>

      <div class="mb-12"></div>

      <div class="mb-8"></div>
      <div>Select up to 5 of your favourite genres</div>
      <div id="spotifyGenre">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete v-model="spotifyGenre" :items="inputSpotifyGenre" label="Genre">
            </v-autocomplete>
          </v-flex>
        </v-layout>
        <div class="mb-4">Drag to Rank</div>
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="1"> Most Favourite </v-col>
          <v-col cols="6">
            <v-card style="padding-left: 10px" max-width="700" class="mx-auto">
              <v-card-text>
                <v-chip-group v-model="spotifyGenre" column active-class="primary--text">
                  <draggable v-model="spotifyGenre" @start="dragStartSGenre" @end="dragEndSGenre">
                    <v-chip v-for="(tag, i) in sGenres" :key="i" draggable>{{
                      tag
                    }}</v-chip>
                  </draggable>
                </v-chip-group>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="1"> Least Favourite </v-col>
          <v-col cols="2"></v-col>
        </v-row>
      </div>

      <div class="mb-12"></div>
      <v-btn text class="success mx-0 mt-3" @click="submit">Let's Go</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  mounted: function () {
    window.scrollTo(0, 0);
  },
  data: () => {
    return {
      name: "",
      youtubeCategory: "",
      bookGenre: "",
      movieGenre: "",
      movieLanguage: [],
      movieImdb: 0,
      spotifyArtist: "",
      spotifyTrack: "",
      spotifyGenre: "",
      youtubes: [],
      books: [],
      movies: [],
      sArtists: [],
      sTracks: [],
      sGenres: [],
      youtubeSelection: null,
      youtubeTag: null,
      bookSelection: null,
      bookTag: null,
      movieSelection: null,
      movieTag: null,
      sArtistSelection: null,
      sArtistTag: null,
      sTrackSelection: null,
      sTrackTag: null,
      sGenreSelection: null,
      sGenreTag: null,
      inputRequiredRule: [(v) => v.length > 0 || "Required"],
      autocompleteMax3Rule: [
        (v) => v.length > 0 || "Required",
        (v) => v.length <= 3 || "Maximum 3 choices",
      ],
      autocompleteMax5Rule: [
        (v) => v.length > 0 || "Required",
        (v) => v.length <= 5 || "Maximum 5 choices",
      ],
      languages: ["English", "Mandarin", "Malay", "Tamil"],
      inputYoutube: [
        "Shorts",
        "Entertainment",
        "News & Politics",
        "Howto & Style",
        "Education",
        "Gaming",
        "Videoblogging",
        "People & Blogs",
        "Comedy",
        "Trailers",
        "Science & Technology",
        "Shows",
        "Sci-Fi/Fantasy",
        "Thriller",
        "Film & Animation",
        "Autos & Vehicles",
        "Music",
        "Horror",
        "Foreign",
        "Pets & Animals",
        "Sports",
        "Travel & Events",
        "Short Movies",
        "Anime/Animation",
        "Movies",
        "Family",
        "Drama",
        "Documentary",
        "Comedy",
        "Classics",
        "Action/Adventure",
      ],
      youtubeCategories: {
        "Sci-Fi/Fantasy": "40",
        Entertainment: "24",
        "Science & Technology": "28",
        Sports: "17",
        "Pets & Animals": "15",
        Music: "10",
        "Action/Adventure": "32",
        Comedy: "34",
        Shows: "43",
        Gaming: "20",
        Classics: "33",
        Shorts: "42",
        "Anime/Animation": "31",
        "Travel & Events": "19",
        "Howto & Style": "26",
        Trailers: "44",
        "Short Movies": "18",
        Thriller: "41",
        "News & Politics": "25",
        Drama: "36",
        Movies: "30",
        Videoblogging: "21",
        Foreign: "38",
        Documentary: "35",
        "Autos & Vehicles": "2",
        "People & Blogs": "22",
        Family: "37",
        Education: "27",
        Horror: "39",
        "Film & Animation": "1",
      },
      inputBook: [
        "Adult",
        "Anthologies",
        "Art",
        "Audiobooks",
        "Biographies",
        "Body",
        "Business",
        "Children",
        "Comics",
        "Contemporary",
        "Cooking",
        "Crime",
        "Engineering",
        "Entertainment",
        "Fantasy",
        "Fiction",
        "Food",
        "Health",
        "History",
        "Horror",
        "Investing",
        "Literary",
        "Literature",
        "Manga",
        "Media-help",
        "Memoirs",
        "Mind",
        "Mystery",
        "Nonfiction",
        "Religion",
        "Romance",
        "Science",
        "Self",
        "Spirituality",
        "Sports",
        "Superheroes",
        "Technology",
        "Thrillers",
        "Travel",
        "Women",
        "Young",
      ],
      inputMovieGenre: [
        "Action",
        "Adult",
        "Adventure",
        "Animation",
        "Biography",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Family",
        "Fantasy",
        "Game-Show",
        "History",
        "Horror",
        "Music",
        "Musical",
        "Mystery",
        "News",
        "Reality-TV",
        "Romance",
        "Sci-Fi",
        "Short",
        "Sport",
        "Talk-Show",
        "Thriller",
        "War",
        "Western",
      ],
      inputMovieLang: [
        "Abkhazian",
        "Aboriginal",
        "Acholi",
        "Afar",
        "Afrikaans",
        "Akan",
        "Albanian",
        "Algonquin",
        "American Sign Language",
        "Amharic",
        "Apache languages",
        "Arabic",
        "Aragonese",
        "Aramaic",
        "Armenian",
        "Aromanian",
        "Assamese",
        "Assyrian Neo-Aramaic",
        "Athapascan languages",
        "Australian Sign Language",
        "Awadhi",
        "Aymara",
        "Azerbaijani",
        "Bable",
        "Baka",
        "Balinese",
        "Bambara",
        "Bashkir",
        "Basque",
        "Bassari",
        "Belarusian",
        "Bemba",
        "Bengali",
        "Berber languages",
        "Bhojpuri",
        "Bicolano",
        "Bislama",
        "Bodo",
        "Bosnian",
        "Brazilian Sign Language",
        "Breton",
        "British Sign Language",
        "Bulgarian",
        "Burmese",
        "Cantonese",
        "Catalan",
        "Central American Indian languages",
        "Chamorro",
        "Chaozhou",
        "Chechen",
        "Cherokee",
        "Cheyenne",
        "Chhattisgarhi",
        "Chinese",
        "Cornish",
        "Corsican",
        "Cree",
        "Creek",
        "Crimean Tatar",
        "Croatian",
        "Crow",
        "Czech",
        "Danish",
        "Dari",
        "Dinka",
        "Divehi",
        "Dogri",
        "Dutch",
        "Dyula",
        "Dzongkha",
        "East-Greenlandic",
        "Eastern Frisian",
        "Egyptian (Ancient)",
        "English",
        "Esperanto",
        "Estonian",
        "Ewe",
        "Faliasch",
        "Faroese",
        "Filipino",
        "Finnish",
        "Flemish",
        "Fon",
        "French",
        "French Sign Language",
        "Frisian",
        "Fulah",
        "Fur",
        "Ga",
        "Gaelic",
        "Galician",
        "Gallegan",
        "Georgian",
        "German",
        "German Sign Language",
        "Greek",
        "Greek, Ancient (to 1453)",
        "Greenlandic",
        "Guarani",
        "Gujarati",
        "Gumatj",
        "Haida",
        "Haitian",
        "Haitian; Haitian Creole",
        "Hakka",
        "Haryanvi",
        "Hassanya",
        "Hausa",
        "Hawaiian",
        "Hebrew",
        "Herero",
        "Himachali",
        "Hindi",
        "Hmong",
        "Hokkien",
        "Hopi",
        "Hungarian",
        "Ibo",
        "Icelandic",
        "Icelandic Sign Language",
        "Igbo",
        "Indian Sign Language",
        "Indonesian",
        "Interlingue",
        "Inuktitut",
        "Inupiaq",
        "Irish",
        "Irula",
        "Italian",
        "Japanese",
        "Japanese Sign Language",
        "Javanese",
        "Jola-Fonyi",
        "Ju'hoan",
        "Kabuverdianu",
        "Kabyle",
        "Kalaallisut",
        "Kalmyk-Oirat",
        "Kannada",
        "Karen",
        "Kashmiri",
        "Kazakh",
        "Khanty",
        "Khasi",
        "Khmer",
        "Kikuyu",
        "Kinyarwanda",
        "Kirghiz",
        "Kirundi",
        "Klingon",
        "Kodava",
        "Konkani",
        "Korean",
        "Korean Sign Language",
        "Kriolu",
        "Kru",
        "Kudmali",
        "Kuna",
        "Kurdish",
        "Ladakhi",
        "Ladino",
        "Lao",
        "Latin",
        "Latvian",
        "Letzeburgesch",
        "Lingala",
        "Lithuanian",
        "Low German",
        "Luxembourgish",
        "Macedonian",
        "Magahi",
        "Maithili",
        "Malagasy",
        "Malay",
        "Malayalam",
        "Malinka",
        "Maltese",
        "Mandarin",
        "Mandingo",
        "Manipuri",
        "Maori",
        "Mapudungun",
        "Marathi",
        "Mari",
        "Marshall",
        "Marshallese",
        "Masai",
        "Maya",
        "Mende",
        "Micmac",
        "Middle English",
        "Min Nan",
        "Minangkabau",
        "Mirandese",
        "Mixtec",
        "Mizo",
        "Mohawk",
        "Moldavian",
        "Mongolian",
        "Montagnais",
        "Morisyen",
        "Nagpuri",
        "Nahuatl",
        "Nama",
        "Navajo",
        "Neapolitan",
        "Nenets",
        "Nepali",
        "Norse, Old",
        "North American Indian",
        "North Ndebele",
        "Northern Sami",
        "Norwegian",
        "Norwegian Nynorsk",
        "Nushi",
        "Nyanja",
        "Occitan",
        "Ojibwa",
        "Ojihimba",
        "Old English",
        "Oriya",
        "Papiamento",
        "Parsee",
        "Pawnee",
        "Persian",
        "Peul",
        "Polish",
        "Polynesian",
        "Portuguese",
        "Pular",
        "Punjabi",
        "Purepecha",
        "Pushto",
        "Quechua",
        "Quenya",
        "Raeto-Romance",
        "Rajasthani",
        "Rhaetian",
        "Romanian",
        "Romany",
        "Russian",
        "Russian Sign Language",
        "Ryukyuan",
        "Saami",
        "Samoan",
        "Sanskrit",
        "Sardinian",
        "Scanian",
        "Scots",
        "Scottish Gaelic",
        "Serbian",
        "Serbo-Croatian",
        "Shanghainese",
        "Shona",
        "Shoshoni",
        "Shuar",
        "Sicilian",
        "Sign Languages",
        "Sindarin",
        "Sindhi",
        "Sinhalese",
        "Sioux",
        "Slovak",
        "Slovenian",
        "Somali",
        "Songhay",
        "Soninke",
        "Sorbian languages",
        "Southern Sotho",
        "Spanish",
        "Spanish Sign Language",
        "Sranan",
        "Sumerian",
        "Swahili",
        "Swati",
        "Swedish",
        "Swiss German",
        "Syriac",
        "Tagalog",
        "Tahitian",
        "Tajik",
        "Tamashek",
        "Tamil",
        "Tarahumara",
        "Tatar",
        "Telugu",
        "Teochew",
        "Thai",
        "Tibetan",
        "Tigrigna",
        "Tigrinya",
        "Tlingit",
        "Tok Pisin",
        "Tonga",
        "Tsonga",
        "Tswana",
        "Tulu",
        "Tupi",
        "Turkish",
        "Turkmen",
        "Tuvinian",
        "Tzotzil",
        "Uighur",
        "Ukrainian",
        "Ukrainian Sign Language",
        "Ungwatsi",
        "Urdu",
        "Uzbek",
        "Vietnamese",
        "Vimeo - Official Chinese Language Version",
        "Visayan",
        "Washoe",
        "Wayuu",
        "Welsh",
        "Wolof",
        "Xhosa",
        "Yakut",
        "Yiddish",
        "Yoruba",
        "Zulu",
      ],
      inputSpotifyArtist: [
        "name1",
        "name2",
        "name3",
        "name4",
        "name5",
        "name6",
        "name7",
        "name8",
        "name9",
        "name10",
        "name11",
      ],
      inputSpotifyTrack: [
        "track1",
        "track2",
        "track3",
        "track4",
        "track5",
        "track6",
        "track7",
        "track8",
        "track9",
        "track10",
        "track11",
      ],
      inputSpotifyGenre: [
        "acoustic",
        "afrobeat",
        "alt-rock",
        "alternative",
        "ambient",
        "anime",
        "black-metal",
        "bluegrass",
        "blues",
        "bossanova",
        "brazil",
        "breakbeat",
        "british",
        "cantopop",
        "chicago-house",
        "children",
        "chill",
        "classical",
        "club",
        "comedy",
        "country",
        "dance",
        "dancehall",
        "death-metal",
        "deep-house",
        "detroit-techno",
        "disco",
        "disney",
        "drum-and-bass",
        "dub",
        "dubstep",
        "edm",
        "electro",
        "electronic",
        "emo",
        "folk",
        "forro",
        "french",
        "funk",
        "garage",
        "german",
        "gospel",
        "goth",
        "grindcore",
        "groove",
        "grunge",
        "guitar",
        "happy",
        "hard-rock",
        "hardcore",
        "hardstyle",
        "heavy-metal",
        "hip-hop",
        "holidays",
        "honky-tonk",
        "house",
        "idm",
        "indian",
        "indie",
        "indie-pop",
        "industrial",
        "iranian",
        "j-dance",
        "j-idol",
        "j-pop",
        "j-rock",
        "jazz",
        "k-pop",
        "kids",
        "latin",
        "latino",
        "malay",
        "mandopop",
        "metal",
        "metal-misc",
        "metalcore",
        "minimal-techno",
        "movies",
        "mpb",
        "new-age",
        "new-release",
        "opera",
        "pagode",
        "party",
        "philippines-opm",
        "piano",
        "pop",
        "pop-film",
        "post-dubstep",
        "power-pop",
        "progressive-house",
        "psych-rock",
        "punk",
        "punk-rock",
        "r-n-b",
        "rainy-day",
        "reggae",
        "reggaeton",
        "road-trip",
        "rock",
        "rock-n-roll",
        "rockabilly",
        "romance",
        "sad",
        "salsa",
        "samba",
        "sertanejo",
        "show-tunes",
        "singer-songwriter",
        "ska",
        "sleep",
        "songwriter",
        "soul",
        "soundtracks",
        "spanish",
        "study",
        "summer",
        "swedish",
        "synth-pop",
        "tango",
        "techno",
        "trance",
        "trip-hop",
        "turkish",
        "work-out",
        "world-music",
      ],
    };
  },
  watch: {
    movieGenre: {
      immediate: true,
      handler(value) {
        if (!this.movies.includes(value) && value != "") {
          this.movies.push(value);
        }
      },
    },
    youtubeCategory: {
      immediate: true,
      handler(value) {
        if (!this.youtubes.includes(value) && value != "") {
          this.youtubes.push(value);
        }
      },
    },
    bookGenre: {
      immediate: true,
      handler(value) {
        if (!this.books.includes(value) && value != "") {
          this.books.push(value);
        }
      },
    },
    spotifyArtist: {
      immediate: true,
      handler(value) {
        if (!this.sArtists.includes(value) && value != "") {
          this.sArtists.push(value);
        }
      },
    },
    spotifyTrack: {
      immediate: true,
      handler(value) {
        if (!this.sTracks.includes(value) && value != "") {
          this.sTracks.push(value);
        }
      },
    },
    spotifyGenre: {
      immediate: true,
      handler(value) {
        if (!this.sGenres.includes(value) && value != "") {
          this.sGenres.push(value);
        }
      },
    },
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        console.log(this.name);
        // console.log(this.youtubeCategory);
        // console.log(this.spotifyArtists);
      }
    },
    dragStartYoutube() {
      if (this.youtubes[this.youtubeSelection]) {
        this.youtubeTag = this.youtubes[this.youtubeSelection];
      } else this.youtubeTag = null;
    },
    dragEndYoutube() {
      if (this.youtubeTag) {
        this.youtubes.forEach((x, i) => {
          if (x === this.youtubeTag) {
            this.youtubeSelection = i;
          }
        });
      }
      console.log(this.youtubes);
    },
    dragStartBook() {
      if (this.books[this.bookSelection]) {
        this.bookTag = this.books[this.bookSelection];
      } else this.bookTag = null;
    },
    dragEndBook() {
      if (this.bookTag) {
        this.books.forEach((x, i) => {
          if (x === this.bookTag) {
            this.bookSelection = i;
          }
        });
      }
    },
    dragStartMovie() {
      if (this.movies[this.movieSelection]) {
        this.movieTag = this.movies[this.movieSelection];
      } else this.movieTag = null;
    },
    dragEndMovie() {
      if (this.movieTag) {
        this.movies.forEach((x, i) => {
          if (x === this.movieTag) this.movieSelection = i;
        });
      }
    },
    dragStartSArtist() {
      if (this.sArtists[this.sArtistSelection]) {
        this.sArtistTag = this.sArtists[this.sArtistSelection];
      } else this.sArtistTag = null;
    },
    dragEndSArtist() {
      if (this.sArtistTag) {
        this.sArtists.forEach((x, i) => {
          if (x === this.currentTag) this.sArtistSelection = i;
        });
      }
    },
    dragStartSTrack() {
      if (this.sTracks[this.sTrackSelection]) {
        this.sTrackTag = this.sTracks[this.sTrackSelection];
      } else this.sTrackTag = null;
    },
    dragEndSTrack() {
      if (this.sTrackTag) {
        this.sTrack.forEach((x, i) => {
          if (x === this.currentTag) this.sTrackSelection = i;
        });
      }
    },
    dragStartSGenre() {
      if (this.sGenres[this.sGenreSelection]) {
        this.sGenreTag = this.sGenres[this.sGenreSelection];
      } else this.sGenreTag = null;
    },
    dragEndSGenre() {
      if (this.sGenreTag) {
        this.sGenres.forEach((x, i) => {
          if (x === this.sGenreTag) this.sGenreSelection = i;
        });
      }
    },
  },
};
</script>

<style>
/* Tooltip container */
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
}

/* Tooltip text */
.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: rgb(90, 90, 90);
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  top: 100%;
  left: 50%;
  margin-left: -60px;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
  visibility: visible;
}

.tooltip .tooltiptext::after {
  content: " ";
  position: absolute;
  bottom: 100%; /* At the top of the tooltip */
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgb(90, 90, 90) transparent;
}
</style>
