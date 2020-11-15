<template>
  <v-container v-if="sendingData == false">
    <VueScrollProgress></VueScrollProgress>
    <v-container fluid justify-center id="main-container">

      <v-form ref="form">

        <p class="text-h4 font-weight-medium my-6">Questionnaire</p>

        <div id="Name">Share your name</div>
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4 mx-4>
            <v-text-field label="Name" v-model="name"></v-text-field>
          </v-flex>
        </v-layout>
        <v-layout>
          <div class="mx-auto mb-4">
            <v-alert color="red" elevation="4" dense outlined type="error" v-if="nameNone">Please Enter Your Name!</v-alert>
          </div>
        </v-layout>
        <div>Share your gender</div>
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4 mx-4>
            <v-radio-group v-model="gender">
              <v-radio v-for="n in genders" :key="n" :label="`${n}`" :value="n"></v-radio>
            </v-radio-group>
          </v-flex>
        </v-layout>

        <v-container id="Youtube" class="category-container">
          <p class="text-h5 font-weight-medium mb-4">Youtube</p>
          <div class="mb-4">Select up to 5 of your favourite Youtube video categories</div>
          <v-layout row wrap justify-center>
            <v-flex xs12 md6 lg4>
              <v-autocomplete v-model="youtubeCategory" :items="inputYoutube" label="Category">
              </v-autocomplete>
            </v-flex>
          </v-layout>
          <div id="ytDisplay" class="rank-display-none">
            <div>Drag to Rank</div>
            <div class="mb-4">(1 - Most Favourite, 5 - Least Favourite)</div>
            <v-layout row wrap justify-center>
              <v-card max-width="700px" width="100%" class="mx-auto mb-5 rank-card">
                <v-card-text class="rank-card-text">
                  <v-chip-group v-model="youtubeSelection" column active-class="primary--text">
                    <draggable v-model="youtubes" @start="dragStartYoutube" @end="dragEndYoutube">
                      <v-chip v-for="(tag, i) in youtubes" :key="i" draggable close @click:close="remove(tag, 'youtubes')" outlined color="rgb(90, 90, 160)">
                        <v-avatar left color="rgb(90, 90, 160)">
                          <span class="color-white">{{i+1}}</span>
                        </v-avatar>
                        {{tag}}
                      </v-chip>
                    </draggable>
                  </v-chip-group>
                </v-card-text>
              </v-card>
            </v-layout>
          </div>
          <v-layout>
            <div class="mx-auto mb-6">
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="ytNone">Please Select At Least ONE!</v-alert>
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="ytExceed">Please Select Maximum FIVE!</v-alert>
            </div>
          </v-layout>
        </v-container>

        <v-container id="Book" class="category-container">
          <p class="text-h5 font-weight-medium mb-4">Books</p>
          <div class="mb-4">Select up to 5 of your favourite book subjects</div>
          <v-layout row wrap justify-center>
            <v-flex xs12 md6 lg4>
              <v-autocomplete v-model="bookGenre" :items="inputBook" label="Genre">
              </v-autocomplete>
            </v-flex>
          </v-layout>
          <div id="bkDisplay" class="rank-display-none">
            <div>Drag to Rank</div>
            <div class="mb-4">(1 - Most Favourite, 5 - Least Favourite)</div>
            <v-layout row wrap justify-center>
              <v-card max-width="700px" width="100%" class="mx-auto mb-5 rank-card">
                <v-card-text>
                  <v-chip-group v-model="bookSelection" column active-class="primary--text">
                    <draggable v-model="books" @start="dragStartBook" @end="dragEndBook">
                      <v-chip v-for="(tag, i) in books" :key="i" draggable close @click:close="remove(tag, 'books')" outlined color="rgb(90, 90, 160)">
                        <v-avatar left color="rgb(90, 90, 160)">
                          <span class="color-white">{{i+1}}</span>
                        </v-avatar>
                        {{tag}}
                      </v-chip>
                    </draggable>
                  </v-chip-group>
                </v-card-text>
              </v-card>
            </v-layout>
          </div>
          <v-layout>
            <div class="mx-auto mb-6">
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="bkNone">Please Select At Least ONE!</v-alert>
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="bkExceed">Please Select Maximum FIVE!</v-alert>
            </div>
          </v-layout>
        </v-container>

        <v-container id="Movie" class="category-container">
          <p class="text-h5 font-weight-medium mb-4">Movies</p>
          <div class="mb-4">Select up to 5 of your favourite Movie Genres</div>
          <v-layout row wrap justify-center>
            <v-flex xs12 md6 lg4>
              <v-autocomplete v-model="movieGenre" :items="inputMovieGenre" label="Genre">
              </v-autocomplete>
            </v-flex>
          </v-layout>
          <div id="mvDisplay" class="rank-display-none">
            <div>Drag to Rank</div>
            <div class="mb-4">(1 - Most Favourite, 5 - Least Favourite)</div>
            <v-layout row wrap justify-center mb-4>
              <v-card max-width="700px" width="100%" class="mx-auto mb-1 rank-card">
                <v-card-text>
                  <v-chip-group v-model="movieSelection" column active-class="primary--text">
                    <draggable v-model="movies" @start="dragStartMovie" @end="dragEndMovie">
                      <v-chip v-for="(tag, i) in movies" :key="i" draggable close @click:close="remove(tag, 'movies')" outlined color="rgb(90, 90, 160)">
                        <v-avatar left color="rgb(90, 90, 160)">
                          <span class="color-white">{{i+1}}</span>
                        </v-avatar>
                        {{tag}}
                      </v-chip>
                    </draggable>
                  </v-chip-group>
                </v-card-text>
              </v-card>
            </v-layout>
          </div>
          <v-layout>
            <div class="mx-auto mb-6">
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="mvNone">Please Select At Least ONE!</v-alert>
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="mvExceed">Please Select Maximum FIVE!</v-alert>
            </div>
          </v-layout>

          <v-layout row wrap justify-center mb-0>
            <v-flex xs12 md6 lg4>
              <div>List your preferred languages</div>
              <v-autocomplete v-model="movieLanguage" :items="inputMovieLang" label="Language" multiple>
                <template #selection="{ item }">
                  <v-chip close color="rgb(90, 90, 160)" outlined @click:close="delLang(item)">{{ item }}</v-chip>
                </template>
              </v-autocomplete>
            </v-flex>
          </v-layout>
          <v-layout>
            <div class="mx-auto mb-12">
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="mvLangNone">Please Select At Least ONE!</v-alert>
            </div>
          </v-layout>

          <v-layout row wrap justify-center mb-8>
            <v-flex xs12 md6 lg4>
              <div>Pick a minimum IMDB value</div>
              <v-slider v-model="movieImdb" :max="10" :min="0" :step="0.1" :thumb-size="30" thumb-label mb-8></v-slider>
            </v-flex>
          </v-layout>
        </v-container>

        <v-container id="Spotify" class="category-container" mb-8>
          <p class="text-h5 font-weight-medium mb-4">Spotify</p>
          <div mb-2>Select up to 3 of your favourite artists</div>
          <v-layout row wrap justify-center>
            <v-flex xs12 md6 lg4>
              <v-text-field v-model="artist" v-on:keyup="searchSpotify(artist, 'artist')" label="Artist"></v-text-field>
              <div v-if="artist">
                <v-btn v-for="suggest in artistSuggestions" :key="suggest" v-on:click="addSpotifyArtist(suggest)" class="suggest-button" small rounded outlined color="blue">{{suggest}}</v-btn>
              </div>
            </v-flex>
          </v-layout>
          <div id="sADisplay" class="rank-display-none">
            <div>Drag to Rank</div>
            <div class="mb-4">(1 - Most Favourite, 3 - Least Favourite)</div>
            <v-layout row wrap justify-center>
              <v-card max-width="700px" width="100%" class="mx-auto mb-5 rank-card">
                <v-card-text>
                  <v-chip-group v-model="sArtistSelection" column active-class="primary--text">
                    <draggable v-model="sArtists" @start="dragStartSArtist" @end="dragEndSArtist">
                      <v-chip v-for="(tag, i) in sArtists" :key="i" draggable close @click:close="remove(tag, 'sArtists')" outlined color="rgb(90, 90, 160)">
                        <v-avatar left color="rgb(90, 90, 160)">
                          <span class="color-white">{{i+1}}</span>
                        </v-avatar>
                        {{tag}}
                      </v-chip>
                    </draggable>
                  </v-chip-group>
                </v-card-text>
              </v-card>
            </v-layout>
          </div>
          <v-layout>
            <div class="mx-auto mb-6">
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="sANone">Please Select At Least ONE!</v-alert>
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="sAExceed">Please Select Maximum THREE!</v-alert>
            </div>
          </v-layout>

          <div class="mb-12"></div>

          <div class="mb-8"></div>
          <div>Select up to 5 of your favourite genres</div>
          <v-layout row wrap justify-center>
            <v-flex xs12 md6 lg4>
              <v-autocomplete v-model="spotifyGenre" :items="inputSpotifyGenre" label="Genre">
              </v-autocomplete>
            </v-flex>
          </v-layout>
          <div id="sGDisplay" class="rank-display-none">
            <div class="mb-4">Drag to Rank</div>
            <div class="mb-4">(1 - Most Favourite, 5 - Least Favourite)</div>
            <v-layout row wrap justify-center mb-4>
              <v-card max-width="700px" width="100%" class="mx-auto mb-1 rank-card">
                <v-card-text>
                  <v-chip-group v-model="sGenreSelection" column active-class="primary--text">
                    <draggable v-model="sGenres" @start="dragStartSGenre" @end="dragEndSGenre">
                      <v-chip v-for="(tag, i) in sGenres" :key="i" draggable close @click:close="remove(tag, 'sGenres')" outlined color="rgb(90, 90, 160)">
                        <v-avatar left color="rgb(90, 90, 160)">
                          <span class="color-white">{{i+1}}</span>
                        </v-avatar>
                        {{tag}}
                      </v-chip>
                    </draggable>
                  </v-chip-group>
                </v-card-text>
              </v-card>
            </v-layout>
          </div>
          <v-layout>
            <div class="mx-auto mb-6">
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="sGNone">Please Select At Least ONE!</v-alert>
              <v-alert color="red" elevation="4" dense outlined type="error" v-if="sGExceed">Please Select Maximum FIVE!</v-alert>
            </div>
          </v-layout>

        </v-container>
        <v-btn color="#5dc0bf" class="mx-0 mb-6 submit-btn" @click="submit()">Let's Go</v-btn>
      </v-form>
    </v-container>
  </v-container>

  <!-- Handle slowest API - Books -->
  <v-main v-else class="color-bg-primary">
    <v-container fluid fill-height>
      <v-layout justify-center align-center>
        <breeding-rhombus-spinner :animation-duration="500" :size="65" color="#ff1d5e" />
        <h1 class="color-white">Running magic calculations...</h1>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
import Vue from "vue";
import draggable from "vuedraggable";
import axios from "axios";
import VueScrollProgress from "vue-scroll-progress";
import { BreedingRhombusSpinner } from "epic-spinners";

Vue.use(VueScrollProgress);

export default {
  components: {
    draggable,
    BreedingRhombusSpinner,
  },
  mounted: function () {
    window.scrollTo(0, 0);
  },
  data: () => {
    return {
      name: "",
      gender: "Male",
      youtubeCategory: "",
      bookGenre: "",
      movieGenre: "",
      movieLanguage: [],
      movieImdb: 0,
      spotifyGenre: "",
      youtubes: [],
      books: [],
      movies: [],
      sArtists: [],
      sGenres: [],
      youtubeSelection: null,
      youtubeTag: null,
      bookSelection: null,
      bookTag: null,
      movieSelection: null,
      movieTag: null,
      sArtistSelection: null,
      sArtistTag: null,
      sGenreSelection: null,
      sGenreTag: null,
      artist: null,
      artistSuggestions: [],
      artistId: null,
      artistIds: [],
      artistDic: {},
      roomCode: localStorage.getItem("roomCode"),
      inputRequiredRule: [(v) => v.length > 0 || "Required"],
      autocompleteMax3Rule: [
        (v) => v.length > 0 || "Required",
        (v) => v.length <= 3 || "Maximum 3 choices",
      ],
      autocompleteMax5Rule: [
        (v) => v.length > 0 || "Required",
        (v) => v.length <= 5 || "Maximum 5 choices",
      ],
      ytNone: false,
      ytExceed: false,
      bkNone: false,
      bkExceed: false,
      mvNone: false,
      mvExceed: false,
      mvLangNone: false,
      sANone: false,
      sAExceed: false,
      sGNone: false,
      sGExceed: false,
      nameNone: false,
      sendingData: false,
      genders: ["Male", "Female"],
      languages: ["English", "Mandarin", "Malay", "Tamil"],
      inputYoutube: [
        "Entertainment",
        "News & Politics",
        "Howto & Style",
        "Education",
        "Gaming",
        "People & Blogs",
        "Comedy",
        "Science & Technology",
        "Film & Animation",
        "Autos & Vehicles",
        "Music",
        "Pets & Animals",
        "Sports",
        "Travel & Events",
      ],
      youtubeCategories: {
        "Film & Animation": "1",
        "Autos & Vehicles": "2",
        Music: "10",
        "Pets & Animals": "15",
        Sports: "17",
        "Travel & Events": "19",
        Gaming: "20",
        "People & Blogs": "22",
        Comedy: "23",
        Entertainment: "24",
        "News & Politics": "25",
        "Howto & Style": "26",
        Education: "27",
        "Science & Technology": "28",
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
        "Afrikaans",
        "Albanian",
        "Apache languages",
        "Arabic",
        "Armenian",
        "Bengali",
        "Cantonese",
        "Catalan",
        "Chinese",
        "Croatian",
        "Czech",
        "Danish",
        "English",
        "Filipino",
        "Finnish",
        "French",
        "German",
        "Greek",
        "Hebrew",
        "Hindi",
        "Hokkien",
        "Hungarian",
        "Indonesian",
        "Irish",
        "Italian",
        "Japanese",
        "Korean",
        "Latin",
        "Latvian",
        "Malay",
        "Malayalam",
        "Mandarin",
        "Mongolian",
        "Persian",
        "Polish",
        "Portuguese",
        "Punjabi",
        "Russian",
        "Scots",
        "Scottish Gaelic",
        "Somali",
        "Spanish",
        "Swedish",
        "Tagalog",
        "Tamil",
        "Thai",
        "Turkish",
        "Ukrainian",
        "Vietnamese",
      ],
      inputSpotifyGenre: [
        "Acoustic",
        "Afrobeat",
        "Alt-Rock",
        "Alternative",
        "Ambient",
        "Anime",
        "Black-Metal",
        "Bluegrass",
        "Blues",
        "Bossanova",
        "Brazil",
        "Breakbeat",
        "British",
        "Cantopop",
        "Chicago-House",
        "Children",
        "Chill",
        "Classical",
        "Club",
        "Comedy",
        "Country",
        "Dance",
        "Dancehall",
        "Death-Metal",
        "Deep-House",
        "Detroit-Techno",
        "Disco",
        "Disney",
        "Drum-And-Bass",
        "Dub",
        "Dubstep",
        "Edm",
        "Electro",
        "Electronic",
        "Emo",
        "Folk",
        "Forro",
        "French",
        "Funk",
        "Garage",
        "German",
        "Gospel",
        "Goth",
        "Grindcore",
        "Groove",
        "Grunge",
        "Guitar",
        "Happy",
        "Hard-Rock",
        "Hardcore",
        "Hardstyle",
        "Heavy-Metal",
        "Hip-Hop",
        "Holidays",
        "Honky-Tonk",
        "House",
        "Idm",
        "Indian",
        "Indie",
        "Indie-Pop",
        "Industrial",
        "Iranian",
        "J-Dance",
        "J-Idol",
        "J-Pop",
        "J-Rock",
        "Jazz",
        "K-Pop",
        "Kids",
        "Latin",
        "Latino",
        "Malay",
        "Mandopop",
        "Metal",
        "Metal-Misc",
        "Metalcore",
        "Minimal-Techno",
        "Movies",
        "Mpb",
        "New-Age",
        "New-Release",
        "Opera",
        "Pagode",
        "Party",
        "Philippines-Opm",
        "Piano",
        "Pop",
        "Pop-Film",
        "Post-Dubstep",
        "Power-Pop",
        "Progressive-House",
        "Psych-Rock",
        "Punk",
        "Punk-Rock",
        "R-N-B",
        "Rainy-Day",
        "Reggae",
        "Reggaeton",
        "Road-Trip",
        "Rock",
        "Rock-N-Roll",
        "Rockabilly",
        "Romance",
        "Sad",
        "Salsa",
        "Samba",
        "Sertanejo",
        "Show-Tunes",
        "Singer-Songwriter",
        "Ska",
        "Sleep",
        "Songwriter",
        "Soul",
        "Soundtracks",
        "Spanish",
        "Study",
        "Summer",
        "Swedish",
        "Synth-Pop",
        "Tango",
        "Techno",
        "Trance",
        "Trip-Hop",
        "Turkish",
        "Work-Out",
        "World-Music",
      ],
    };
  },
  computed: {
    firstError() {
      if (this.nameNone == true) {
        return 0;
      } else if (this.ytNone == true || this.ytExceed == true) {
        return "#Youtube";
      } else if (this.bkNone == true || this.bkExceed == true) {
        return "#Book";
      } else if (
        this.mvNone == true ||
        this.mvExceed == true ||
        this.mvLangNone == true
      ) {
        return "#Movie";
      } else if (
        this.sANone == true ||
        this.sAExceed == true ||
        this.sGNone == true ||
        this.sGExceed == true
      ) {
        return "#Spotify";
      } else {
        return "";
      }
    },
  },
  watch: {
    movieGenre: {
      immediate: true,
      handler(value) {
        if (
          !this.movies.includes(value) &&
          value != "" &&
          typeof value != "undefined"
        ) {
          this.changeRankElementToInline("mvDisplay");
          this.movies.push(value);
          this.$nextTick(() => {
            this.movieGenre = undefined;
          });
        }
      },
    },
    youtubeCategory: {
      immediate: true,
      handler(value) {
        if (
          !this.youtubes.includes(value) &&
          value != "" &&
          typeof value != "undefined"
        ) {
          this.changeRankElementToInline("ytDisplay");
          this.youtubes.push(value);
          this.$nextTick(() => {
            this.youtubeCategory = undefined;
          });
        }
      },
    },
    bookGenre: {
      immediate: true,
      handler(value) {
        if (
          !this.books.includes(value) &&
          value != "" &&
          typeof value != "undefined"
        ) {
          this.changeRankElementToInline("bkDisplay");

          this.books.push(value);
          this.$nextTick(() => {
            this.bookGenre = undefined;
          });
        }
      },
    },
    spotifyGenre: {
      immediate: true,
      handler(value) {
        if (
          !this.sGenres.includes(value) &&
          value != "" &&
          typeof value != "undefined"
        ) {
          this.changeRankElementToInline("sGDisplay");
          this.sGenres.push(value);
          this.$nextTick(() => {
            this.spotifyGenre = undefined;
          });
        }
      },
    },
    movies: {
      immediate: true,
      handler() {
        if (this.movies == []) {
          this.changeRankElementToNone("sADisplay");
        }
      },
    },
  },
  methods: {
    submit() {
      if (this.validate()) {
        this.sendQuestionnaireData();
      } else {
        this.showAlerts();
        this.$nextTick(() => {
          this.$vuetify.goTo(this.firstError);
        });
      }
    },
    delLang(item) {
      this.movieLanguage = this.movieLanguage.filter(function (e) {
        return e !== item;
      });
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
          if (x === this.sArtistTag) this.sArtistSelection = i;
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
    searchSpotify(query, type) {
      axios({
        url: "/spotify-token",
        method: "GET",
      }).then((auth) => {
        axios({
          method: "GET",
          url: "https://api.spotify.com/v1/search",
          params: {
            q: query,
            type: type,
            limit: 5,
          },
          headers: auth.data,
        }).then((response) => {
          if (type === "artist") {
            // artists > items > name
            let items = response.data.artists.items;
            let names = [];
            for (let i = 0; i < items.length; i++) {
              names.push(items[i]["name"]);
              this.artistDic[items[i]["name"]] = items[i]["id"];
            }
            this.artistSuggestions = names;
          }
        });
      });
    },
    addSpotifyArtist(value) {
      if (!this.sArtists.includes(value) && value != "" && value != undefined) {
        this.changeRankElementToInline("sADisplay");
        this.sArtists.push(value);
        this.$nextTick(() => {
          this.artist = undefined;
        });
      }
    },
    changeRankElementToNone(id) {
      let display = document.getElementById(id);
      display.classList.remove("rank-display-inline");
      display.classList.add("rank-display-none");
    },
    changeRankElementToInline(id) {
      let display = document.getElementById(id);
      display.classList.remove("rank-display-none");
      display.classList.add("rank-display-inline");
    },
    sendQuestionnaireData() {
      // make spotify genres all lowercase
      this.sendingData = true;
      let spotify_genres = this.sGenres;
      let spotify_genres_lower = [];
      for (let genre of spotify_genres) {
        spotify_genres_lower.push(genre.toLowerCase());
      }

      // process to get youtube video ids
      let youtubes = this.youtubes;
      let youtubes_id = [];
      for (let youtube of youtubes) {
        if (youtube in this.youtubeCategories) {
          youtubes_id.push(this.youtubeCategories[youtube]);
        }
      }
      // process to get ids of spotify artists
      for (let artist of this.sArtists) {
        let id = this.artistDic[artist];
        this.artistIds.push(id);
      }

      // process gender
      var genderData = "";
      if (this.gender == "Male") genderData = "M";
      else genderData = "F";

      axios({
        url: "/add-questionnaire/" + this.roomCode,
        method: "POST",
        data: {
          name: this.name,
          youtube: youtubes_id,
          book: this.books,
          movie: {
            genre: this.movies,
            imdb: this.movieImdb,
            language: this.movieLanguage,
          },
          spotify: {
            genre: spotify_genres_lower,
            artist: this.artistIds,
          },
          gender: genderData,
        },
      }).then(() => {
        window.location.href = "/dashboard/" + this.roomCode;
      });
    },
    remove(tag, list) {
      if (list == "youtubes") {
        this.youtubes = this.youtubes.filter(function (e) {
          return e !== tag;
        });
        if (this.youtubes.length == 0) {
          this.changeRankElementToNone("ytDisplay");
        }
      } else if (list == "books") {
        this.books = this.books.filter(function (e) {
          return e !== tag;
        });
        if (this.books.length == 0) {
          this.changeRankElementToNone("bkDisplay");
        }
      } else if (list == "movies") {
        this.movies = this.movies.filter(function (e) {
          return e !== tag;
        });
        if (this.movies.length == 0) {
          this.changeRankElementToNone("mvDisplay");
        }
      } else if (list == "sArtists") {
        this.sArtists = this.sArtists.filter(function (e) {
          return e !== tag;
        });
        if (this.sArtists.length == 0) {
          this.changeRankElementToNone("sADisplay");
        }
      } else if (list == "sGenres") {
        this.sGenres = this.sGenres.filter(function (e) {
          return e !== tag;
        });
        if (this.sGenres.length == 0) {
          this.changeRankElementToNone("sGDisplay");
        }
      }
    },
    validate() {
      this.resetAlerts();
      if (
        this.youtubes.length == 0 ||
        this.movies.length == 0 ||
        this.books.length == 0 ||
        this.movieLanguage.length == 0 ||
        this.sArtists.length == 0 ||
        this.sGenres.length == 0 ||
        this.name == "" ||
        this.youtubes.length > 5 ||
        this.movies.length > 5 ||
        this.books.length > 5 ||
        this.sArtists.length > 3 ||
        this.sGenres.length > 5
      ) {
        return false;
      }
      return true;
    },
    showAlerts() {
      if (this.name == "") this.nameNone = true;

      if (this.youtubes.length == 0) this.ytNone = true;
      else if (this.youtubes.length > 5) this.ytExceed = true;

      if (this.books.length == 0) this.bkNone = true;
      else if (this.books.length > 5) this.bkExceed = true;

      if (this.movies.length == 0) this.mvNone = true;
      else if (this.movies.length > 5) this.mvExceed = true;

      if (this.movieLanguage.length == 0) this.mvLangNone = true;

      if (this.sArtists.length == 0) this.sANone = true;
      else if (this.sArtists.length > 3) this.sAExceed = true;

      if (this.sGenres.length == 0) this.sGNone = true;
      else if (this.sGenres.length > 5) this.sGExceed = true;
    },
    resetAlerts() {
      this.ytNone = false;
      this.ytExceed = false;
      this.mvNone = false;
      this.mvExceed = false;
      this.bkNone = false;
      this.bkExceed = false;
      this.mvLangNone = false;
      this.sANone = false;
      this.sAExceed = false;
      this.sGNone = false;
      this.sGExceed = false;
      this.nameNone = false;
    },
  },
};
</script>

<style lang="scss">
@import "~@/styles/colors";

.suggest-button {
  margin-right: 10px;
  margin-bottom: 10px;
}

#main-container {
  margin-top: 56px;
}

#progress-container-el {
  /* background */
  background-color: transparent !important;
  margin-top: 48px;
}
#progress-el {
  /* progress bar */
  background-color: $highlight1 !important;
  height: 6px !important;
}

.category-container {
  margin-top: 24px;
  margin-bottom: 24px;
}
.rank-display {
  &-none {
    display: none;
  }
  &-inline {
    display: inline;
  }
}
.rank-card {
  padding-left: 10px;
}
.rank-card-text {
  align-items: center;
}

.submit-btn {
  color: $white !important;
}
</style>
