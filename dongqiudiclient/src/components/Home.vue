<template>
  <div class="home">
    <el-form label-position="right" label-width="80px" >
      <el-form-item label="联赛">
        <el-select v-model="legacy" placeholder="选择联赛" style="display: block" @change="onLegaciesChange">
          <el-option v-for="item in alllaeagues"
          :key="item.league_id"
          :value="item.api"
          :label="item.label"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="比赛">
        <el-select v-model="selectedMatch" placeholder="请选择比赛" style="display: block">
          <el-option v-for="item in matches"
            :key="item.match_id"
            :value="item.match_id"
            :label="item.team_A_name + 'vs' + item.team_B_name + item.beijingTime"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form>
        <el-button @click="onSubmit">确定</el-button>
      </el-form>
    </el-form>
    <a :href="downloadUrl" target="_blank" v-if="showDownload">下载</a>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { Form, FormItem, Row, Col, Button, Select, Option } from 'element-ui'
import { getAllLegacies, getAllMatches } from '@/api/dongqiudi'
@Component
export default class Home extends Vue {
  private alllaeagues = []
  private legacy = ''
  private matches = []
  private selectedMatch = ''

  private downloadUrl = ''
  private showDownload = false
  private onSubmit () {
    this.downloadUrl = `api/getexceltemplate?url=${this.legacy}&matchid=${this.selectedMatch}`
    this.showDownload = true
  }

  private onLegaciesChange (value: any) {
    getAllMatches(value).then(res => {
      this.matches = res.data
    })
  }
  private mounted () {
    getAllLegacies().then(res => {
      this.alllaeagues = res.data
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  width: 600px;
  margin: 0 auto;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
