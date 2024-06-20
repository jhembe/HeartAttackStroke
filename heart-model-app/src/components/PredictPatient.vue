<template>
  <div class="container">
    <h1>Patient Prediction Form</h1>
    <form @submit.prevent="getPrediction" class="prediction-form">
      <div class="form-group">
        <label for="age">Age</label>
        <input v-model.number="age" placeholder="Enter age" id="age" required />
      </div>

      <div class="form-group">
        <label for="sex">Gender</label>
        <select v-model.number="sex" id="sex" required>
          <option :value="0">Male</option>
          <option :value="1">Female</option>
        </select>
      </div>

      <div class="form-group">
        <label for="cp">Chest Pain Type</label>
        <select v-model.number="cp" id="cp" required>
          <option :value="0">Typical Angina</option>
          <option :value="1">Atypical Angina</option>
          <option :value="2">Non-Anginal Pain</option>
          <option :value="3">Asymptomatic</option>
        </select>
      </div>

      <div class="form-group">
        <label for="trtbps">Resting Blood Pressure</label>
        <input v-model.number="trtbps" placeholder="Enter resting blood pressure" id="trtbps" required />
      </div>

      <div class="form-group">
        <label for="chol">Total Cholesterol</label>
        <input v-model.number="chol" placeholder="Enter total cholesterol" id="chol" required />
      </div>

      <div class="form-group">
        <label for="fbs">Fasting Blood Sugar</label>
        <input v-model.number="fbs" placeholder="Enter fasting blood sugar" id="fbs" required />
      </div>

      <div class="form-group">
        <label for="restecg">Resting Electrocardiogram</label>
        <select v-model.number="restecg" id="restecg" required>
          <option :value="0">Normal</option>
          <option :value="1">ST-T Wave Abnormality</option>
          <option :value="2">Left Ventricular Hypertrophy</option>
        </select>
      </div>

      <div class="form-group">
        <label for="thalachh">Maximum Heart Rate Achieved</label>
        <input v-model.number="thalachh" placeholder="Enter maximum heart rate" id="thalachh" required />
      </div>

      <div class="form-group">
        <label for="exng">Exercise Induced Angina</label>
        <select v-model.number="exng" id="exng" required>
          <option :value="0">No</option>
          <option :value="1">Yes</option>
        </select>
      </div>

      <div class="form-group">
        <label for="oldpeak">Oldpeak</label>
        <input v-model.number="oldpeak" placeholder="Enter oldpeak" id="oldpeak" required />
      </div>

      <div class="form-group">
        <label for="slp">Slope of Peak Exercise ST Segment</label>
        <select v-model.number="slp" id="slp" required>
          <option :value="0">Upsloping</option>
          <option :value="1">Flat</option>
          <option :value="2">Downsloping</option>
        </select>
      </div>

      <div class="form-group">
        <label for="caa">Number of Major Blood Vessels</label>
        <select v-model.number="caa" id="caa" required>
          <option :value="0">0</option>
          <option :value="1">1</option>
          <option :value="2">2</option>
          <option :value="3">3</option>
        </select>
      </div>

      <div class="form-group">
        <label for="thall">Thallium Stress Test</label>
        <input v-model.number="thall" placeholder="Enter thallium stress test result" id="thall" required />
      </div>

      <button type="submit" class="submit-button">Predict</button>
    </form>

    <transition name="fade">
      <div v-if="prediction" class="prediction-result">
        Prediction: {{ prediction }}
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      age: null,
      sex: null,
      cp: null,
      trtbps: null,
      chol: null,
      fbs: null,
      restecg: null,
      thalachh: null,
      exng: null,
      oldpeak: null,
      slp: null,
      caa: null,
      thall: null,
      prediction: null,
    };
  },
  methods: {
    async getPrediction() {
      const features = {
        age: this.age,
        sex: this.sex,
        cp: this.cp,
        trtbps: this.trtbps,
        chol: this.chol,
        fbs: this.fbs,
        restecg: this.restecg,
        thalachh: this.thalachh,
        exng: this.exng,
        oldpeak: this.oldpeak,
        slp: this.slp,
        caa: this.caa,
        thall: this.thall,
      };

      try {
        const response = await axios.post('http://localhost:5000/predict', features);
        this.prediction = response.data.prediction;
      } catch (error) {
        console.error("There was an error with the prediction:", error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

.prediction-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group select:focus {
  border-color: #007bff;
  outline: none;
}

.submit-button {
  padding: 10px 20px;
  background: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
}

.submit-button:hover {
  background: #0056b3;
}

.prediction-result {
  margin-top: 20px;
  padding: 10px;
  background: #e9ecef;
  border-left: 5px solid #007bff;
  font-size: 18px;
  color: #333;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
</style>
