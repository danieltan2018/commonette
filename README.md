# Commonette

An all-in-one recommendation platform that allows users to get recommendations for music, videos and books based on the aggregated preferences of a group, and without the need to provide their listen/watch history. 



Try a live demo [here](commonette.smusis.com).

TO ADD: Watch our youtube [video](https://youtu.be/rct3AHYej5U).



## Setup - Backend

1. Go to backend folder

   ```bash
   $ cd backend
   ```

2. Install required libraries

   ```bash
   $ pip install -r requirements.txt 
   ```

3. Run backend application

   ```bash
   $ python app.py
   ```

4. Copy backend url



## Setup - Frontend

1. Go to app folder

   ```bash
   $ cd app
   ```

2. Setup project and install libraries

   ```bash
   $ npm install
   ```

3. Update backend url on `line 12` in `app/src/main.js` 

   ```javascript
   // update link with backend url
   Vue.prototype.$http.defaults.baseURL = "https://commonapi.smusis.com";  
   ```

4. Compile and run

   ```bash
   $ npm run serve
   ```





## Contributors

### Contributors on GitHub

- [Daniel](https://github.com/danieltan2018)
- [Kai Min](https://github.com/KaiminOng)
- [Sui Ling](https://github.com/SuiLing237)
- [Syafiqah](https://github.com/syafiqahmr)
- [Yao Ying](https://github.com/suicidal-muffin)



## Acknowledgements

- [Responsive Landing Page](https://github.com/bedimcode/responsive-landing-page-coffee3d)
- [Cartoon Vectors](https://www.freepik.com/vectors/cartoon)
- [People Vectors](https://www.freepik.com/vectors/people)
- [Nezuko Image](https://www.zerochan.net/2579685)
- [Tanjiro Image](https://www.zerochan.net/2579684)



## Version

- Version 1.0
