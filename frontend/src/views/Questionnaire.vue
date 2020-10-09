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
			<div id="youtube1">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="First Choice" v-model="youtubeCategory1" :items="inputYoutube" :rules="inputRequiredRule"></v-autocomplete>
					</v-flex> 
				</v-layout>
				<div id="youtube1btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="youtubeShow2">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
				</div>
			</div>
				
			<div id="youtube2" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Second Choice" v-model="youtubeCategory2" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="youtube2btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="youtubeShow3">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove2">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="youtube3" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Third Choice" v-model="youtubeCategory3" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="youtube3btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="youtubeShow4">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove3">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="youtube4" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Fourth Choice" v-model="youtubeCategory4" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="youtube4btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="youtubeShow5">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove4">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="youtube5" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Fifth Choice" v-model="youtubeCategory5" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="youtube5btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove5">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>
			<div class="mb-12"></div>
			<!-- <v-layout row wrap justify-center mb-8>
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
			</v-layout> -->

			<!-- START OF TESTING (KAIMIN) -->
			<v-layout row wrap justify-center>
				<v-flex xs12 md6 lg4>
					<v-autocomplete
					v-model="youtubeCategory"
					:items="inputYoutube"
					label="Language"
					multiple
					chips
					deletable-chips
					:rules="autocompleteMax5Rule"
					>
					</v-autocomplete>
				</v-flex>
			</v-layout>
			<div class="mb-4"> Drag to Rank</div>
			<div id="app">
				Most Favourite
				<v-card style="padding-left:10px" max-width="110" class="mx-auto"> 
					<v-card-text>
						<v-chip-group v-model="youtubeCategory" column active-class="primary--text">
							<draggable v-model="youtubeCategory" @start="dragStart" @end="dragEnd">
								<v-chip v-for="(tag, i) in youtubeCategory" :key="i" draggable>{{ tag }}</v-chip>
							</draggable>
						</v-chip-group>
					</v-card-text>
				</v-card>
				Least Favourite
			</div>
			<div class="mb-12"></div>
			<!-- END OF TESTING (KAIMIN) -->

			<h2 class="mb-4">Books</h2>
			<div>Select up to 5 of your favourite book subjects</div>

			<!-- START OF TESTING (KAIMIN) -->
			<div id="book1">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="First Choice" v-model="bookCategory1" :items="inputYoutube"></v-autocomplete>
					</v-flex> 
				</v-layout>
				<div id="book1btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="bookShow2">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
				</div>
			</div>
				
			<div id="book2" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Second Choice" v-model="bookCategory2" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="book2btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="bookShow3">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove2">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="book3" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Third Choice" v-model="bookCategory3" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="book3btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="bookShow4">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove3">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="book4" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Fourth Choice" v-model="bookCategory4" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="book4btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="bookShow5">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove4">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="book5" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Fifth Choice" v-model="bookCategory5" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="book5btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove5">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>
			<!-- END OF TESTING (KAIMIN) -->

			<div class="mb-12"></div>

			<h2 class="mb-4">Movies</h2>
			<div>Select up to 5 of your favourite movie genres</div>

			<!-- START OF TESTING (KAIMIN) -->
			<div id="movie1">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="First Choice" v-model="movieCategory1" :items="inputYoutube" :rules="inputRequiredRule"></v-autocomplete>
					</v-flex> 
				</v-layout>
				<div id="movie1btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="movieShow2">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
				</div>
			</div>
				
			<div id="movie2" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Second Choice" v-model="movieCategory2" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="movie2btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="movieShow3">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove2">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="movie3" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Third Choice" v-model="movieCategory3" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="movie3btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="movieShow4">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove3">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="movie4" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Fourth Choice" v-model="movieCategory4" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="movie4btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip"  @click="movieShow5">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
						</span>
						<span class="tooltiptext">Add Row</span>
					</button>
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove4">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>

			<div id="movie5" style="display:none">
				<v-layout row wrap justify-center>
					<v-flex xs12 md6 lg4>
						<v-autocomplete label="Fifth Choice" v-model="movieCategory5" :items="inputYoutube"></v-autocomplete>
					</v-flex>
				</v-layout>
				<div id="movie5btn">
					<button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove5">
						<span class="v-btn__content">
							<i aria-hidden="true" class="v-icon notranslate theme--dark">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
									<path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
							</svg></i>
						</span>
						<span class="tooltiptext">Remove Row</span>
					</button>
				</div>
			</div>
			<!-- END OF TESTING (KAIMIN) -->
			<div class="mb-12"></div>

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
					:max="10"
					:min="0"
					:step="0.1"
					:thumb-size="30"
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
import draggable from 'vuedraggable';
export default {
	components: {
		draggable,
	},
	data:()=>{
		return {
			name: '',
			movieLanguage: [],
			movieImdb: 0,
			youtubeCategory: [],
			spotifyArtists: [],
			spotifyTracks: [],
			spotifyGenres: [],
			youtubeCategory1: '',
			youtubeCategory2: '',
			youtubeCategory3: '',
			youtubeCategory4: '',
			youtubeCategory5: '',
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
			inputYoutube: ["cat1","cat2", "cat3", "cat4", "cat5", "cat6","cat7", "cat8", "cat9", "cat11", "cat10"],
			selection: null,
			currentTag: null
		}
	},
	methods: {
		submit(){
			if (this.$refs.form.validate()){
				console.log(this.name);
				console.log(this.youtubeCategory);
				console.log(this.spotifyArtists);
			}
		},
		dragStart() {
		if (this.youtubeCategory2[this.selection]) this.currentTag = this.youtubeCategory2[this.selection];
		else this.currentTag = null;
		},
		dragEnd() {
			var self = this;
			if (this.currentTag) {
				this.youtubeCategory2.forEach((x, i) => {
				if (x.name === self.currentTag) self.selection = i;
				});  
			}
		},
		bookShow2(){
			document.getElementById("book2").style.display = "inline";
			document.getElementById("book1btn").style.display = "none";
		},
		bookShow3(){
			document.getElementById("book3").style.display = "inline";
			document.getElementById("book2btn").style.display = "none";
		},
		bookShow4(){
			document.getElementById("book4").style.display = "inline";
			document.getElementById("book3btn").style.display = "none";
		},
		bookShow5(){
			document.getElementById("book5").style.display = "inline";
			document.getElementById("book4btn").style.display = "none";
		},
		bookRemove2(){
			this.bookCategory2 = "";
			document.getElementById("book2").style.display = "none";
			document.getElementById("book1btn").style.display = "inline";
		},
		bookRemove3(){
			this.bookCategory3 = "";
			document.getElementById("book3").style.display = "none";
			document.getElementById("book2btn").style.display = "inline";
		},
		bookRemove4(){
			this.bookCategory4 = "";
			document.getElementById("book4").style.display = "none";
			document.getElementById("book3btn").style.display = "inline";
		},
		bookRemove5(){
			this.bookCategory5 = "";
			document.getElementById("book5").style.display = "none";
			document.getElementById("book4btn").style.display = "inline";
		},
		movieShow2(){
			document.getElementById("movie2").style.display = "inline";
			document.getElementById("movie1btn").style.display = "none";
		},
		movieShow3(){
			document.getElementById("movie3").style.display = "inline";
			document.getElementById("movie2btn").style.display = "none";
		},
		movieShow4(){
			document.getElementById("movie4").style.display = "inline";
			document.getElementById("movie3btn").style.display = "none";
		},
		movieShow5(){
			document.getElementById("movie5").style.display = "inline";
			document.getElementById("movie4btn").style.display = "none";
		},
		movieRemove2(){
			this.movieCategory2 = "";
			document.getElementById("movie2").style.display = "none";
			document.getElementById("movie1btn").style.display = "inline";
		},
		movieRemove3(){
			this.movieCategory3 = "";
			document.getElementById("movie3").style.display = "none";
			document.getElementById("movie2btn").style.display = "inline";
		},
		movieRemove4(){
			this.movieCategory4 = "";
			document.getElementById("movie4").style.display = "none";
			document.getElementById("movie3btn").style.display = "inline";
		},
		movieRemove5(){
			this.movieCategory5 = "";
			document.getElementById("movie5").style.display = "none";
			document.getElementById("movie4btn").style.display = "inline";
		},
		youtubeShow2(){
			document.getElementById("youtube2").style.display = "inline";
			document.getElementById("youtube1btn").style.display = "none";
		},
		youtubeShow3(){
			document.getElementById("youtube3").style.display = "inline";
			document.getElementById("youtube2btn").style.display = "none";
		},
		youtubeShow4(){
			document.getElementById("youtube4").style.display = "inline";
			document.getElementById("youtube3btn").style.display = "none";
		},
		youtubeShow5(){
			document.getElementById("youtube5").style.display = "inline";
			document.getElementById("youtube4btn").style.display = "none";
		},
		youtubeRemove2(){
			this.youtubeCategory2 = "";
			document.getElementById("youtube2").style.display = "none";
			document.getElementById("youtube1btn").style.display = "inline";
		},
		youtubeRemove3(){
			this.youtubeCategory3 = "";
			document.getElementById("youtube3").style.display = "none";
			document.getElementById("youtube2btn").style.display = "inline";
		},
		youtubeRemove4(){
			this.youtubeCategory4 = "";
			document.getElementById("youtube4").style.display = "none";
			document.getElementById("youtube3btn").style.display = "inline";
		},
		youtubeRemove5(){
			this.youtubeCategory5 = "";
			document.getElementById("youtube5").style.display = "none";
			document.getElementById("youtube4btn").style.display = "inline";
		}
	}
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
  bottom: 100%;  /* At the top of the tooltip */
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgb(90, 90, 90) transparent;
}
</style>
