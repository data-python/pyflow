import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
const prefix = `monaco-editor/esm/vs`;

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue()
    ],
    build: {
        outDir: './dist',
        rollupOptions: {
            output: {
                // https://juejin.cn/post/6933463466111926286
                manualChunks: {
                    jsonWorker: [`${prefix}/language/json/json.worker`],
                    cssWorker: [`${prefix}/language/css/css.worker`],
                    htmlWorker: [`${prefix}/language/html/html.worker`],
                    tsWorker: [`${prefix}/language/typescript/ts.worker`],
                    editorWorker: [`${prefix}/editor/editor.worker`],
                },
            },
        },
    }
})
