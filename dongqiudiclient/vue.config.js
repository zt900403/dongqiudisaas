'use strict'
const path = require('path')
function resolve (dir) {
  return path.resolve(__dirname, dir)
}

// const publicPath = process.env.NODE_ENV === 'production' ? '/public/dist/' : '/'
const publicPath = process.env.NODE_ENV === 'production' ? '/' : '/'
module.exports = {
  configureWebpack: {
    // resolve: {
    //   alias: {
    //     '@': resolve('src'),
    //     stylus: resolve('src/styles/stylus')
    //   }
    // }
    // devServer: {
    //   before (app) {
    //     const data = require('./mock/data.json')
    //     const seller = data.seller
    //     app.get('/api/seller', (req, res) => {
    //       res.json({
    //         errno: 0,
    //         data: seller
    //       })
    //     })
    //   }
    // }
  },
  devServer: {
    proxy: 'http://localhost:5000'
  },
  publicPath
}
