import request from '@/utils/request'

export const getAllLegacies = () =>
  request({
    url: 'api/getallleagues',
    method: 'get'
  })

export const getAllMatches = (url: string) =>
  request({
    url: '/api/getallmatches',
    method: 'get',
    params: {
      url
    }
  })
