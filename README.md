# bert_test_1n8g
<html>
<body>
<!--StartFragment--><!DOCTYPE html><figure class="md-table-fig md-expand md-focus" cid="n39" mdtype="table" style="box-sizing: border-box; margin: 1.2em 0px; overflow-x: auto; max-width: calc(100% + 16px); padding: 0px; cursor: default; color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">

NVIDIA_GeForce_RTX_3080_Ti | master@59b64db | rank_per_process @59b64db | naive@59b64db
-- | -- | -- | --
LibAI_bert_large_pretrain_graph nl24_nah16_hs1024_FP16_actrue DP2_MP2_PP2_zerofalse_stage0_mbs32_gbs512_acc8_1n8g | building graph Done! Cost time: 19.14s.    building plan Done! Cost time: 18.08s. node0 : 6029-6738MIB | building plan Done! Cost time: 17.91s. building graph Done! Cost time: 18.9 s. node0 :  6026-6728MIB | building plan Done! Cost time: 18.14s.   building graph Done! Cost time: 18.99s.   node0 : 6598-6728MIB

</figure><br class="Apple-interchange-newline"><!--EndFragment-->
</body>
</html>


- 全局loss曲线对比

![LibAI_bert_large_pretrain_graph_nl24_nah16_hs1024_FP16_actrue_DP2_MP2_PP2_zerofalse_stage0_mbs32_gbs512_acc8_1n8g,png](https://user-images.githubusercontent.com/86536994/229665268-7308888f-6009-4134-84e7-32c8df7cbcd2.png)

- 50步loss曲线对比

![LibAI_bert_large_pretrain_graph_nl24_nah16_hs1024_FP16_actrue_DP2_MP2_PP2_zerofalse_stage0_mbs32_gbs512_acc8_1n8g_50_220,png](https://user-images.githubusercontent.com/86536994/229665753-0ffc2f22-b413-483f-b7e7-c016341da707.png)
- 100步loss曲线对比

![LibAI_bert_large_pretrain_graph_nl24_nah16_hs1024_FP16_actrue_DP2_MP2_PP2_zerofalse_stage0_mbs32_gbs512_acc8_1n8g_100_220,png](https://user-images.githubusercontent.com/86536994/229665787-89d524f7-70af-48d4-bd47-a5a363ce3a36.png)
