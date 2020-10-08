import { required } from  'vuelidate/lib/validators'

<template>
    <v-container fluid justify-center>
		<v-layout row wrap justify-center>
			<v-flex xs12 md6>
				<h1>Let's get to know you!</h1>
			</v-flex>
		</v-layout>
		<v-form ref="form">
			<v-layout row wrap justify-center mb-8>
				<v-flex xs12 md6 lg4>
					<v-text-field label="Name" v-model="name" :rules="inputRequiredRule"></v-text-field>
				</v-flex>
			</v-layout>
			<h2 class="mb-4">Youtube</h2>
			<div> Select up to 5 of your favourite Youtube video cateogories</div>
			<v-layout row wrap justify-center mb-8>
				<v-flex xs12 md6 lg4>
					<v-autocomplete
					v-model="youtubeCategory"
					:items="inputYoutube"
					label="Language"
					multiple
					chips
					deletable-chips
					:rules="autocompleteMax5Rule"
					></v-autocomplete>
				</v-flex>
			</v-layout>
			<h2 class="mb-4">Books</h2>
			<div>Select up to 5 of your favourite book subjects</div>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="First Choice" v-model="bookCategory1" :items="inputYoutube" :rules="inputRequiredRule"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Second Choice" v-model="bookCategory2" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Third Choice" v-model="bookCategory4" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Fourth Choice" v-model="bookCategory4" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center mb-8>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Fifth Choice" v-model="bookCategory5" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<h2 class="mb-4">Movies</h2>
			<div>Select up to 5 of your favourite movie genres</div>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="First Choice" v-model="movieCategory1" :items="inputYoutube" :rules="inputRequiredRule"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Second Choice" v-model="movieCategory2" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Third Choice" v-model="movieCategory3" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Fourth Choice" v-model="movieCategory4" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center mb-4>
				<v-flex xs12 md6 lg4>
					<v-autocomplete label="Fifth Choice" v-model="movieCategory5" :items="inputYoutube"></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center mb-8>
				<v-flex xs12 md6 lg4>
					<div>List your preferred languages</div>
					<v-autocomplete
					v-model="movieLanguage"
					:items="languages"
					label="Language"
					multiple
					chips
					deletable-chips
					:rules="inputRequiredRule"
					></v-autocomplete>
				</v-flex>
			</v-layout>
			<v-layout row wrap justify-center mb-8>
				<v-flex xs12 md6 lg4>
					<div>Pick a minimum IMDB value</div>
					<v-slider
					v-model="movieImdb"
					:thumb-size="24"
					thumb-label
					mb-8
					></v-slider>
				</v-flex>
			</v-layout>
			<h2 class="mb-4">Spotify</h2>
			<v-layout row wrap justify-center mt-4 mb-4>
				<v-flex xs12 md6 lg4>
					<div>Select up to 3 of your favourite artists</div>
					<v-autocomplete
					v-model="spotifyArtists"
					:items="languages"
					label="Artists"
					multiple
					chips
					deletable-chips
					:rules="autocompleteMax3Rule"
					></v-autocomplete>
				</v-flex>
			</v-layout>		
			<v-layout row wrap justify-center mb-4>
				<v-flex xs12 md6 lg4>
					<div>Select up to 3 of your favourite tracks</div>
					<v-autocomplete
					v-model="spotifyTracks"
					:items="languages"
					label="Tracks"
					multiple
					chips
					deletable-chips
					:rules="autocompleteMax3Rule"
					></v-autocomplete>
				</v-flex>
			</v-layout>	
			<v-layout row wrap justify-center mb-8>
				<v-flex xs12 md6 lg4>
					<div>Select up to 5 of your favourite genres</div>
					<v-autocomplete
					v-model="spotifyGenres"
					:items="languages"
					label="Genres"
					multiple
					chips
					deletable-chips
					:rules="autocompleteMax5Rule"
					></v-autocomplete>
				</v-flex>
			</v-layout>			
			<v-btn text class="success mx-0 mt-3" @click="submit">Let's Go</v-btn>
		</v-form>
    </v-container>
</template>

<script>
export default {
  data: () => {
		return {
			name: '',
			movieLanguage: [],
			movieImdb: 0,
			youtubeCategory: [],
			spotifyArtists: [],
			spotifyTracks: [],
			spotifyGenres: [],
			bookCategory1: '',
			bookCategory2: '',
			bookCategory3: '',
			bookCategory4: '',
			bookCategory5: '',
			movieCategory1: '',
			movieCategory2: '',
			movieCategory3: '',
			movieCategory4: '',
			movieCategory5: '',
			inputRequiredRule:[
				v => v.length > 0 || 'Required'
			],
			autocompleteMax3Rule:[
				v => v.length > 0|| 'Required',
				v => v.length <= 3 || 'Maximum 3 choices'
			],
			autocompleteMax5Rule:[
				v => v.length > 0  || 'Required',
				v => v.length <= 5 || 'Maximum 5 choices'
			],
			languages: ["English", "Mandarin", "Malay", "Tamil"],
			inputYoutube: ["cat1","cat2", "cat3", "cat4", "cat5", "cat6","cat7", "cat7", "cat9", "cat11", "cat10"]
		}
	},
	methods: {
		submit(){
			if (this.$refs.form.validate()){
				console.log(this.name);
				console.log(this.youtubeCategory);
				console.log(this.spotifyArtists);
			}
		}
	}
};
</script>