# Bloom

- https://www.kaggle.com/code/julianschelb/finetune-bloom-token-classification

BLOOM uses a decoder-only transformer model architecture modified from Megatron-LM GPT-2.


```
BloomConfig = {
  "_name_or_path": "bigscience/bloom-560m",
  "apply_residual_connection_post_layernorm": false,
  "architectures": [
    "BloomForCausalLM"
  ],
  "attention_dropout": 0.0,
  "attention_softmax_in_fp32": true,
  "bias_dropout_fusion": true,
  "bos_token_id": 1,
  "eos_token_id": 2,
  "hidden_dropout": 0.0,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "layer_norm_epsilon": 1e-05,
  "masked_softmax_fusion": true,
  "model_type": "bloom",
  "n_head": 16,
  "n_inner": null,
  "n_layer": 24,
  "offset_alibi": 100,
  "pad_token_id": 3,
  "pretraining_tp": 1,
  "skip_bias_add": true,
  "skip_bias_add_qkv": false,
  "slow_but_exact": false,
  "transformers_version": "4.26.0",
  "unk_token_id": 0,
  "use_cache": true,
  "vocab_size": 250880
}
```

----

```commandline
$ll /home/henry/opt_weights/bloom-560m-np/*
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.input_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.input_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.mlp.dense_4h_to_h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.mlp.dense_4h_to_h.weight
-rw-rw-r-- 1 henry henry      8320 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.mlp.dense_h_to_4h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.mlp.dense_h_to_4h.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.post_attention_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.post_attention_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.self_attention.dense.bias
-rw-rw-r-- 1 henry henry   2097280 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.self_attention.dense.weight
-rw-rw-r-- 1 henry henry      6272 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.self_attention.query_key_value.bias
-rw-rw-r-- 1 henry henry   6291584 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.0.self_attention.query_key_value.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.input_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.input_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.mlp.dense_4h_to_h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.mlp.dense_4h_to_h.weight
-rw-rw-r-- 1 henry henry      8320 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.mlp.dense_h_to_4h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.mlp.dense_h_to_4h.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.post_attention_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.post_attention_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.self_attention.dense.bias
-rw-rw-r-- 1 henry henry   2097280 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.self_attention.dense.weight
-rw-rw-r-- 1 henry henry      6272 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.self_attention.query_key_value.bias
-rw-rw-r-- 1 henry henry   6291584 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.10.self_attention.query_key_value.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.input_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.input_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.mlp.dense_4h_to_h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.mlp.dense_4h_to_h.weight
-rw-rw-r-- 1 henry henry      8320 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.mlp.dense_h_to_4h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.mlp.dense_h_to_4h.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.post_attention_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.post_attention_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.self_attention.dense.bias
-rw-rw-r-- 1 henry henry   2097280 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.self_attention.dense.weight
-rw-rw-r-- 1 henry henry      6272 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.self_attention.query_key_value.bias
-rw-rw-r-- 1 henry henry   6291584 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.11.self_attention.query_key_value.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.input_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.input_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.mlp.dense_4h_to_h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.mlp.dense_4h_to_h.weight
-rw-rw-r-- 1 henry henry      8320 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.mlp.dense_h_to_4h.bias
-rw-rw-r-- 1 henry henry   8388736 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.mlp.dense_h_to_4h.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.post_attention_layernorm.bias
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.post_attention_layernorm.weight
-rw-rw-r-- 1 henry henry      2176 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.self_attention.dense.bias
-rw-rw-r-- 1 henry henry   2097280 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.self_attention.dense.weight
-rw-rw-r-- 1 henry henry      6272 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.self_attention.query_key_value.bias
-rw-rw-r-- 1 henry henry   6291584 Mar  5 19:32 /home/henry/opt_weights/bloom-560m-np/h.12.self_attention.query_key_value.weight

```

----

```
BloomForTokenClassification(
  (transformer): BloomModel(
    (word_embeddings): Embedding(250880, 1024)
    (word_embeddings_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
    (h): ModuleList(
      (0): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (1): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (2): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (3): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (4): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (5): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (6): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (7): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (8): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (9): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (10): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (11): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (12): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (13): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (14): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (15): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (16): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (17): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (18): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (19): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (20): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (21): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (22): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
      (23): BloomBlock(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (self_attention): BloomAttention(
          (query_key_value): Linear(in_features=1024, out_features=3072, bias=True)
          (dense): Linear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (mlp): BloomMLP(
          (dense_h_to_4h): Linear(in_features=1024, out_features=4096, bias=True)
          (gelu_impl): BloomGelu()
          (dense_4h_to_h): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
    )
    (ln_f): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
  )
  (dropout): Dropout(p=0.0, inplace=False)
  (classifier): Linear(in_features=1024, out_features=2, bias=True)
)

```